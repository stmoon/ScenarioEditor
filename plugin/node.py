
class Node (object) :

    def __init__(self, id, name='') :
        self._properties = dict()
        self.setProperty('id', id)
        if name is '' :
            self.setProperty('name', 'n' + str(id))
        else :
            self.setProperty('name', name)
        self.setProperty('init_pos', [0,0,0])
        self.setProperty('takeoff_time', 0.0)
        self.setProperty('takeoff_height', 0.5)
        self.setProperty('landing_time', 0.0)

        self._traj = dict()     # [time, x, y, z]
        self._color = []        # [time, type, speed, Red, Green, Blue, Brightness]
        self._events = dict()   # [event_type, id, time, event_data ...]  # not working

    def property(self, name) :
        return self._properties[name]

    def setProperty(self, name, value) :
        self._properties[name] = value

    def id(self) :
        return self.property('id')

    def name(self) :
        return self.property('name')

    def initPosition(self, x, y, z):
        self.setProperty("init_pos", [x,y,z])

    def lastPos(self):
        traj = self.trajectory()
        if len(traj) is 0 :
            init_pos = self.property('init_pos')
            takeoff_height = self.property('takeoff_height')
            return [init_pos[0], init_pos[1], takeoff_height]
        else :
            return traj[-1][1:4]

    def addTraj(self, scenario, traj):
        self._traj[scenario] =  traj

    def showTraj(self):
        for scen in self._traj :
            print(self._traj[scen])

    def pos(self, time):
        if time == 0 :
            init_pos = self.property('init_pos')
            takeoff_height = self.property('takeoff_height')
            return [init_pos[0], init_pos[1], takeoff_height]

        traj = self.trajectory()
        for t in traj :
            if t[0] is time :
                return t[1:3]

    def trajectory(self):
        traj = []

        for scen in self._traj :
            traj += self._traj[scen]

        traj.sort()
        return traj

    def color(self):
        self._color.sort()
        return self._color

    def setColor(self, time, color_data):
        self._color.append([time] + color_data)

    def setTakeoff(self, time, height):
        self._takeoff = [time, height]
        self.setProperty('takeoff_time', time)
        self.setProperty('takeoff_height', height)

        init_pos = self.property('init_pos')
        init_pos[2] = height
        self.setProperty('init_pos', init_pos)

    def setLanding(self, time):
        self.setProperty('landing_time', time)

    def takeoff(self):
        return (self.property('takeoff_time'), self.property('takeoff_height'))

    def landing(self):
        return self.property('landing_time')

    def addEvent(self, type, time, event_data):
        if not time in self._events.keys():
            self._events[time] = []
        self._events[time].append([type, self.id(), time] + event_data)

    def events(self):
        return self._events
