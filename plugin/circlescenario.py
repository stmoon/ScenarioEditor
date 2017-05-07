from scenario import *
import numpy as np

class CircleScenario (IScenarioPlugin) :

    def __init__(self, start_time, end_time) :
        IScenarioPlugin.__init__(self, start_time, end_time)

	self._properties['center_point'] = [0,0,0]
        self._properties['radius'] = 10
        self._properties['speed'] = 0.1	    # m/s
        self._properties['rate'] = 10	    # Hz
	self._properties['trans_start_point'] = [0,0,0]
	self._properties['trans_end_point'] = [0,0,0]

    def update(self) :
	pass
