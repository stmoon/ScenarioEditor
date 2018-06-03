import node
import numpy as np
from numpy.linalg import inv
import math
from pyquaternion import Quaternion

class IScenario (object):

    _nodes = None                 # node trajectory for each node
    _init_node_pos = None
    _properties = None            # specific properties for specific scenario
    _traj = None                  # scenario trajectory
    _traj_hist = None             # scenario trajectory history

    def __init__(self, start_time, end_time, traj=None) :
        self._nodes = dict()
        self._init_node_pos = dict()
        self._properties = dict()
        if traj == None :
            self._traj = list()
            self._traj_hist = list()
        else :
            self._traj = traj

        self._properties['start_time']  = start_time
        self._properties['end_time']  = end_time
        self._properties['trans'] = [0.0, 0.0, 0.0]
        self._properties['rot_direct'] = [1.0, 0.0, 0.0]
        self._properties['rot_center'] = [0.0, 0.0, 0.0]
        self._properties['rot_angle'] = 0.0
        self._properties['is_moving'] = True
        self._nodes = {}

    def addNode(self, nodes, init_pos=0.0):
        SCEN_INTERVAL = 0.1  # 0.1 m

        # make node_list
        # (the parameter nodes can be list of Node objects or a Node object)
        node_list = []
        if isinstance(nodes, list) is True :
            node_list = nodes
        else :
            node_list.append(nodes)

        # add node
        for node in node_list :
            if not node in self._nodes :
                self._nodes[node] = list()
                self._init_node_pos[node] = init_pos / SCEN_INTERVAL
            else :
                print("ERR: already the node was added")

    def nodes(self) :
        return self._nodes

    def scenarioTrajectory(self):
        return self._traj

    def trajHistory(self):
        return self._traj_hist

    def property(self, name) :
        return self._properties[name]

    def setProperty(self, name, value) :
        self._properties[name] = value

    # ==DEPRECATED== output : list of scenario format
    def scenario(self, node) :
        output = list()

        traj = self.trajectory(node)
        for i in traj :
            time  = i[0]
            pos_x = i[1]
            pos_y = i[2]
            pos_z = i[3]
            str = '<move id=%d> %f,%f,%f </move>' % (node.id(), pos_x, pos_y, pos_z)
            output.append([time,str])

        return output

    # output : list of [time,x,y,z]
    def trajectory(self, node=None) :
        if node is None :
            return self._nodes
        elif node in self._nodes :
            return self._nodes[node]
        else :
            return False

    # specific scenario (child class) should implement update method 
    def compile(self) :
        # init trajectory
        self._traj = []

        # append current node position
        len_nodes = len(self.nodes())
        for i, node in zip(range(len_nodes), self.nodes()):
            self._traj.append(node.lastPos())
            self._init_node_pos[node] = i

    # generate node trajectory based on scenario trajectory
    def run(self):

        SCEN_FREQ     = 10      # 10 Hz
        TRAJ_INTERVAL = 0.1     # 10 Hz
        SCEN_INTERVAL = 0.1     # 0.1 m

        # get properties
        start_time = self._properties['start_time']
        end_time = self._properties['end_time']
        duration = end_time - start_time
        rot_center = np.array(self._properties['rot_center'], dtype='float32')
        rot_angle = self._properties['rot_angle'] * TRAJ_INTERVAL / duration
        rot_direct = np.array(self._properties['rot_direct'], dtype='float32')
        trans = np.array(self._properties['trans'], dtype='float32')
        is_moving = self._properties['is_moving']

        if is_moving is True :
            step = len(self._traj) / (duration * SCEN_FREQ)
        else :
            step = 0

        # check node
        if self._nodes is None :
            print("ERR: there is no node")
            return False

        if len(self._traj) is 0 :
            print("ERR: there is no trajectory")
            return False

        # reset node trajectory
        for node in self.nodes() :
            self._nodes[node] = list()

        # reset trajectory history
        self._traj_hist = []

        # init index of scenario buffer for node
        index_node = dict()
        for node in self.nodes() :
            index_node[node] = self._init_node_pos[node]

        # calculate part of H
        t = trans / (duration * SCEN_FREQ)
        r = rot_direct / np.linalg.norm(rot_direct)
        theta = math.radians(rot_angle)
        q = Quaternion(axis=r.tolist(), angle=theta)
        r = q.rotation_matrix
        b = np.array([[0,0,0,1]])

        one = np.array([[1]*len(self._traj)]).T
        traj = np.concatenate([self._traj, one], axis=1)

        # generate node trajectory
        for i in range(int(duration*SCEN_FREQ)) :
            time = start_time + i * TRAJ_INTERVAL

            # change trajectory
            T2 = np.c_[np.eye(3), t.T]
            T2 = np.r_[T2, b]

            R1 = np.c_[r, np.zeros((3, 1))]
            R1 = np.r_[R1, b]

            T1 = np.c_[np.eye(3), -rot_center.T - t.T*i]
            T1 = np.r_[T1, b]

            H = inv(T1) @ R1 @ T1 @ T2

            traj = (H @ traj.T).T
            self._traj_hist.append(traj[:, 0:3])

            # check end of routine
            end_state = False
            for node in self.nodes() :
                ix = index_node[node]
                if len(traj) <= ix :
                    end_state = True
            if end_state is True :
                break

            # append trajectory to buffer
            for node in self.nodes() :
                ix = index_node[node]
                pos = traj[int(ix)]
                self._nodes[node].append([time, pos[0], pos[1], pos[2]])
                index_node[node] = ix + step

        # update trajectory of node
        for node in self.nodes() :
            node.addTraj(self, self._nodes[node])

    def changeColor(self, time, color_data):
        for node in self.nodes() :
            node.setColor(time, color_data)

    def __add__(self, other) :

        start_time = self._properties['start_time']
        end_time = other._properties['end_time']
        self.compile()
        other.compile()

        # merge trajectory but remove duplicated values
        traj = self.scenarioTrajectory()[:-1] + other.scenarioTrajectory()

        return IScenario(start_time, end_time, traj=traj)
