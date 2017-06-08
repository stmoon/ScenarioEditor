import node

class IScenarioPlugin (object):

    _nodes = {}                 # trajectory for each node
    _properties = {}            # specific properties for specific scenario
    
    def __init__(self, start_time, end_time) :
        self._properties['start_time']  = start_time
        self._properties['end_time']  = end_time
        self._nodes = {}

    def addNode(self, node):
        if not node in self._nodes :
            self._nodes[node] = list()
            return True
        else :
            return False

    def property(self, name) :
        return self._properties[name]
    
    def setProperty(self, name, value) :
        self._properties[name] = value

    # output : list of scenario format 
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
    def update(self) :
        raise NotImplementedError
