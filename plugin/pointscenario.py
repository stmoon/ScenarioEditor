from scenario import *
import numpy as np

class PointScenario (IScenarioPlugin) :

    _nodeName = ''

    def __init__(self, start_time, end_time) :
        IScenarioPlugin.__init__(self, start_time, end_time)

	self._properties['start_point'] = [0,0,0]
	self._properties['end_point'] = [0,0,0]

    # PointScenario is for single node
    def addNode(self, name):
        if len(self._nodes) is 0 :
            self._nodeName = name
            return IScenarioPlugin.addNode(self, name)
        else :
            return False

    def update(self) :
        if self._nodeName is '':
            return False

        start_point = np.array(self._properties['start_point'], dtype='float32')
        end_point = np.array(self._properties['end_point'], dtype='float32')
        start_time = self._properties['start_time']
        end_time = self._properties['end_time']

        self._nodes[self._nodeName].append([start_time, start_point[0], start_point[1], start_point[2]])
        self._nodes[self._nodeName].append([end_time, end_point[0], end_point[1], end_point[2]])
