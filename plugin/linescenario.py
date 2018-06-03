from scenario import *
import numpy as np


class LineScenario (IScenario) :

    _node = None

    def __init__(self, start_time, end_time) :
        IScenario.__init__(self, start_time, end_time)

        self._properties['start_point'] = [0, 0, 0]
        self._properties['end_point'] = [0, 0, 0]
        self._properties['rate'] = 10

    def compile(self) :

        # get value
        start_point = np.array(self._properties['start_point'], dtype='float32')
        end_point = np.array(self._properties['end_point'], dtype='float32')
        rate = self._properties['rate']
        start_time = self._properties['start_time']
        end_time = self._properties['end_time']
        duration = end_time - start_time

        # init trajectory
        self._traj = []

        # update scenario trajectory
        u = (end_point - start_point)
        u = u / np.linalg.norm(u) / 10.0
        norm_u = np.linalg.norm(u)

        self._traj.append(start_point)
        while ( np.linalg.norm(self._traj[-1] -  end_point) > norm_u ) :
            t = self._traj[-1]
            self._traj.append(t + u)