from scenario import *
import numpy as np


class LineScenario (IScenarioPlugin) :

    _nodeName = ''

    def __init__(self, start_time, end_time) :
        IScenarioPlugin.__init__(self, start_time, end_time)

        self._properties['start_point'] = [0, 0, 0]
        self._properties['end_point'] = [0, 0, 0]
        self._properties['rate'] = 10

    def addNode(self, name):
        if len(self._nodes) is 0 :
            self._nodeName = name
            return IScenarioPlugin.addNode(self, name)
        else :
            return False

    def update(self) :
        if self._nodeName is '' :
            return False

        start_point = np.array(self._properties['start_point'], dtype='float32')
        end_point = np.array(self._properties['end_point'], dtype='float32')
        rate = self._properties['rate']
        start_time = self._properties['start_time']
        end_time = self._properties['end_time']
        duration = end_time - start_time

        alpha = (end_point - start_point) / (rate*duration)

        for i in xrange(int(rate*duration)) :
            time = start_time + i * (1.0/rate)
            traj = alpha * i + start_point
            self._nodes[self._nodeName].append([time, traj[0], traj[1], traj[2]])

        self._nodes[self._nodeName].append([end_time, end_point[0], end_point[1], end_point[2]])

