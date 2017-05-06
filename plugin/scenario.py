
class IScenarioPlugin :

    _nodes = {}                 # trajectory for each node
    _properties = {}            # specific properties for specific scenario
    
    def __init__(self, start_time, end_time) :
        self._properties['start_time']  = start_time
        self._properties['end_time']  = end_time

    def addNode(self, name):
        if not name in self._nodes :
            self._nodes[name] = list()
            return True
        else :
            return False

    def property(self, name) :
        return self._properties[name]
    
    def setProperty(self, name, value) :
        self._properties[name] = value

    # output : list of scenario format 
    def scenario(self, node_name) :
        pass

    # output : list of [x,y,z]
    def trajectory(self, name) :
        return self._nodes[name]

    # specific scenario (child class) should implement update method 
    def update(self) :
        raise NotImplementedError
