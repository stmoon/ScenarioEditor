class IScenarioPlugin :

    _start_time = 0             # scenario start time
    _end_time = 0               # scenario end time
    _nodes = {}                 # trajectory for each node
    _properties = {}            # specific properties for specific scenario
    
    def __init__(self, start_time, end_time) :
        self._properties['start_time']  = start_time
        self._properties['end_time']  = end_time        
    
    def property(self, name) :
        return self._properties[name]
    
    def setPropery(self, name, value) :
        self._properties[name] = value

    # output : list of scenario format 
    def scenario(self, node_name) :
        pass

    # output : list of [x,y,z]
    def trajectory(self, name) :
        return _node[name]

    # specific scenario (child class) should implement update method 
    def update(self) :
        raise NotImplementedError
