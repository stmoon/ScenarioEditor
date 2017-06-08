import collections

_output = dict()

def clear() :
    _output.clear()
    
def addTrajectory(traj) :
    global _output
    for node in traj :
        for t in traj[node] :
            if  not t[0] in _output.keys() :
                _output[t[0]] = []
            _output[t[0]].append([node.id(),t[1:]])

def printXML() :
    global _output
    _output = collections.OrderedDict(sorted(_output.items()))
    for time in _output :
        str = "<scenario time=%f> " % (time)
        print str
        for v in _output[time] :
            str = '<move id=%d> %f,%f,%f </move>' % (v[0], v[1][0], v[1][1], v[1][2])
            print str
        str = "</scenario>"
        print str
