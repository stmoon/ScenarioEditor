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

        start_point = np.array(self._properties['start_point'], dtype='float32')
        end_point = np.array(self._properties['end_point'], dtype='float32')
        rate = self._properties['rate']
        start_time = self._properties['start_time']
        end_time = self._properties['end_time']
        duration = end_time - start_time
	
	# init
	np.array([[
	
	# rotation 
        for i in xrange(int(rate*duration)) :
            time = start_time + i * (1.0/rate)

            #self._nodes[self._node].append([time, traj[0], traj[1], traj[2]])
