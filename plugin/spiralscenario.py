from scenario import *
import numpy as np
import math
import matplotlib.pyplot as plt

class SpiralScenario (IScenario) :

    _node = None

    def __init__(self, start_time, end_time) :
        IScenario.__init__(self, start_time, end_time)

        self._properties['start_point'] = [5, 0, 0]
        self._properties['center_point'] = [5, 0, 0]
        self._properties['speed'] = 0.1	    # m/s
        self._properties['rate'] = 10	    # Hz
        self._properties['height'] = 10
        self._properties['twist_number'] = 5


    def compile(self) :

       # step1.  make spiral path

        start = np.array(self._properties['start_point'], dtype='float32')
        center = np.array(self._properties['center_point'], dtype='float32')
        start = np.array([start])
        center = np.array([center])
        rate = self._properties['rate']
        num = 500
        height = self._properties['height']
        dense = self._properties['twist_number']

        p1 = np.array(start - center)
        rad = np.linalg.norm(p1)

        i = (p1 / rad).T
        j = np.dot([[0, -1, 0], [1, 0, 0], [0, 0, 0]], i)
        k = np.cross(i.T, j.T).T

        i = i / np.linalg.norm(i)
        j = j / np.linalg.norm(j)
        k = k / np.linalg.norm(k)

        dcm = np.concatenate([i, j, k], axis=1)


        pi = np.array([])
        path_list = []

        index = height * num


        for i in range(index - 1):
            i = index -i # to change start point from center to outside
            rate =  1/index * i
            degree = ( (2* dense * np.pi)/ index ) * i

            s_path = np.array( [rad - (rad*rate) * np.cos(degree),   rad - (rad*rate) * np.sin(degree),  height - (i / index) * height])
            p = np.concatenate([s_path, [1]], axis=0).reshape(1, 4)

            if pi.size is 0 :
                pi = p
            else :
                pi = np.append(pi, p, axis=0)

        H = np.concatenate([dcm, center.T], axis=1)
        H = np.concatenate([H, [[0, 0, 0, 1]]], axis=0)

        temp_traj = np.dot(H, pi.T).T
        # self._traj = temp_traj[:,0:3].tolist() // for using a final equi- distance path
        path_list = temp_traj[:,0:3].T


    # step2.  get distance list between two points

        cum = 0
        target = 0.1
        target_dis = 1    # target equi-distance level, change this value
        min_value = 1000000

        path_dis = []
        final_path = []

        for i in range(index - 2):
            path_dis =  np.sqrt ( (path_list[0,i+1]-path_list[0,i])**2 + (path_list[1,i+1]-path_list[1,i])**2 + (path_list[2,i+1]-path_list[2,i])**2 )
            final_path.append(path_dis)



    # step3.  make euqi distance path
        len_path = len(final_path)
        sum_path = []

        for i,c in zip(final_path,range(len_path)):
            cum = cum + i
            sum_path.append([i,cum])


        cum = 0
        target_c = 0
        target_list =[]

        for i, c in zip(final_path, range(len_path)):
            cum = cum + i
            gap = target - cum

            if abs(gap) < min_value:
                min_value = abs(gap)
                target_c = c

            if gap < 0.0:

                target = target + target_dis
                min_value = abs(target - cum)
                target_c = c
                target_list.append(target_c)

        self._traj = temp_traj[target_list,0:3].tolist()


       # step4.  check equi-

        # for i in range(len(target_list)-2):
        #     print( np.sqrt ( (temp_traj[target_list[i+1],0]-temp_traj[target_list[i],0])**2 + (temp_traj[target_list[i+1],1]-temp_traj[target_list[i],1])**2 + (temp_traj[target_list[i]+1,2]-temp_traj[target_list[i],2])**2 ))





