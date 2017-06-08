
class Node (object) :
    _name = ""
    _id = 0
    traj = list()

    def __init__(self, id, name='') :
        self._id = id
        if name is '' :
            self._name = 'n'+str(id)
        else :
            self._name = name

    def id(self) :
        return self._id

    def name(self) :
        return self._name

