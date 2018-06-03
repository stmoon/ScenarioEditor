from scenario import *
import numpy as np
import math

class CircleScenario (IScenario) :

    _node = None

    def __init__(self, start_time, end_time) :
        IScenario.__init__(self, start_time, end_time)

        self._properties['center_point'] = [ 0, 0, 0 ]
        self._properties['start_point'] = [0, 0, 0]
        self._properties['angle'] = 0
        self._properties['speed'] = 0.1	    # m/s
        self._properties['rate'] = 10	    # Hz


    def compile(self) :

        # get value
        start = np.array(self._properties['start_point'], dtype='float32')
        center = np.array(self._properties['center_point'], dtype='float32')
        start = np.array([start])
        center = np.array([center])
        angle_x = self._properties['angle']/2
        rate = self._properties['rate']
        len_inter  = 0.1

        # step1 : generate p1 = c-s vector

        p1 = np.array(start - center)
        rad = np.linalg.norm(p1)


        # step2 : generate i,j,k base vertor & DCM matrix

        i = (p1/rad).T
        j = np.dot([[0,-1,0],[1,0,0],[0,0,0]],i)
        k = np.cross(i.T,j.T).T

        i = i / np.linalg.norm(i)
        j = j / np.linalg.norm(j)
        k = k / np.linalg.norm(k)

        dcm = np.concatenate([i, j, k], axis=1)

        # step3 : generate circle path
        theta = np.rad2deg( np.arcsin(len_inter / (rad* 2)) *2 )
        index = int(360 // theta)

        pi = np.array([])
        for i in range(int(index+2)):
            c_path = np.array( [ rad * np.cos(np.deg2rad(theta*i)), rad* np.sin(np.deg2rad(theta*i)),0] )
            p =  np.concatenate([c_path, [1]], axis=0). reshape(1,4)


            if pi.size is 0 :
                pi = p
            else :
                pi = np.append(pi, p, axis=0)

        # step4 : generate H vector : dcm, center,null vector
        H = np.concatenate([dcm, center.T], axis=1)
        H = np.concatenate([H, [[0, 0, 0, 1]]], axis=0)

        traj  = np.dot(H, pi.T).T
        self._traj = traj[:,0:3].tolist()
