#############################################
# The test scenario for connect
#############################################

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

def test_2() :

    node1 = Node(1)
    node1.initPosition(1,1,0)

    node2 = Node(1)
    node2.initPosition(2,1,0)

    node3 = Node(1)
    node3.initPosition(3,1,0)

    
    test1 = [node1, node2, node3]
    s1 = IScenario(0,1)
    s1.addNode(test1)


    
    node1.initPosition(1,1,0)
    node2.initPosition(1,2,0)
    node3.initPosition(1,3,0)

    s2 = IScenario(2,1)
    s2.addNode(test1)

    
    connect_scenario(s1,s2)

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
