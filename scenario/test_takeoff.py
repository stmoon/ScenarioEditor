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
    for i in range(30) :
        x = (i%5)*3.0
        y = int(i/5)*3.0
        node = Node(i+1)
        node.setProperty('takeoff_height', 1.0)
        node.initPosition(x,y,0)
        nodes.append(node)

    ## Takeoff
    for n in nodes[0:10]:
        n.setProperty('takeoff_time', 5.0)

    for n in nodes[10:20]:
        n.setProperty('takeoff_time', 10.0)

    for n in nodes[20:30]:
        n.setProperty('takeoff_time', 15.0)
    
    ## S1-1 Scenario
    group1 = nodes[0:5] + nodes[10:15] + nodes[20:25]
    start_time, end_time = util.nextScenTime(20.0, 10)
    s1 = IScenario(start_time, end_time)
    s1.setProperty('trans', [3.0, 0.0, 0.0])
    s1.setProperty('is_moving', False)
    s1.addNode(group1)
    s1.changeColor(0.0, [0,0, 0, 255, 0,200])
    s1.compile()
    s1.run()

    ## S1-2 Scenario
    group2 = nodes[5:10] + nodes[15:20] + nodes[25:30]
    start_time, end_time = util.nextScenTime(20.0, 10)
    s2 = IScenario(start_time, end_time)
    s2.setProperty('trans', [-3.0, 0.0, 0.0])
    s2.setProperty('is_moving', False)
    s2.addNode(group2)
    s2.changeColor(0.0, [0,0,255, 0, 0, 200])
    s2.compile()
    s2.run()

    ## S2-1 Scenario
    group1 = nodes[0:5] + nodes[10:15] + nodes[20:25]
    start_time, end_time = util.nextScenTime(35.0, 10)
    s1 = IScenario(start_time, end_time)
    s1.setProperty('trans', [-3.0, 0.0, 0.0])
    s1.setProperty('is_moving', False)
    s1.addNode(group1)
    s1.changeColor(0.0, [0,0, 0, 255, 0,200])
    s1.compile()
    s1.run()

    ## S2-2 Scenario
    group2 = nodes[5:10] + nodes[15:20] + nodes[25:30]
    start_time, end_time = util.nextScenTime(35.0, 10)
    s2 = IScenario(start_time, end_time)
    s2.setProperty('trans', [3.0, 0.0, 0.0])
    s2.setProperty('is_moving', False)
    s2.addNode(group2)
    s2.changeColor(0.0, [0,0,255, 0, 0, 200])
    s2.compile()
    s2.run()


    ## Landing
    start_time, end_time = util.nextScenTime(50.0, 10)
    for i in range(30) :
        nodes[i].setLanding(end_time)


    output.outputXML("./takeoff.sc", nodes)

    util.showNodeTrajectory(nodes)


if __name__ == "__main__":
    takeoffTest()
