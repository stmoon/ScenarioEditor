import sys
sys.path.append("../plugin/")


import scenario
import output
from linescenario import *
from pointscenario import *
from circlescenario import *
from spiralscenario import *
from node import *
from connect import *
import util

def takeoffTest() :

    nodes = []
    for i in range(5) :
        y = (i%5)*3.0
        x = int(i/5)*3.0
        node = Node(i+1)
        node.setProperty('takeoff_height', 1.0)
        node.initPosition(x,y,0)
        nodes.append(node)

    ## Takeoff
    for n in nodes[0:5]:
        n.setProperty('takeoff_time', 1.0)

    ## Scenario1
    #start_time, end_time = util.nextScenTime(1,  3) 
    #s1 = IScenario(start_time, end_time)
    #s1.setProperty('is_moving', False)
    #s1.setProperty("trans", [0.0, 2.0, 0.0])
    #s1.addNode(nodes)
    #s1.compile()
    #s1.run()


    ## Scenario2
    start_time, end_time = util.nextScenTime(4,  10) 
    s2 = IScenario(start_time, end_time)
    s2.setProperty('is_moving', False)
    s2.setProperty("trans", [0.0, 10.0, 0.0])
    s2.setProperty("rot_center", [0,0,1])
    s2.setProperty("rot_angle", 90)
    s2.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s2.addNode(nodes)
    s2.compile()
    s2.run()

    ## Landing
    #start_time, end_time = util.nextScenTime(15.0, 5)
    #for i in range(5) :
    #    nodes[i].setLanding(end_time)


    output.outputXML("./test1.sc", nodes)

    util.showNodeTrajectory(nodes)


if __name__ == "__main__":
    takeoffTest()
