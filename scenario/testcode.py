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
    
    ## S1 Scenario
    start_time, end_time = util.nextScenTime(20.0, 10)
    s1 = IScenario(start_time, end_time)
    s1.setProperty('trans', [1.0, 0.0, 0.0])
    s1.setProperty('is_moving', False)
    s1.addNode(nodes)
    s1.changeColor(0.0, [0,0,255, 0, 0,200])
    s1.compile()
    s1.run()


    ## Landing
    start_time, end_time = util.nextScenTime(30.0, 10)
    for i in range(30) :
        nodes[i].setLanding(end_time)


    output.outputXML("./takeoff.sc", nodes)

    util.showNodeTrajectory(nodes)



def linecircleTest() :

    node1 = Node(1, 'n1')
    node2 = Node(2, 'n2')
    node3 = Node(3, 'n3')

    l1 = LineScenario(0.0, 10.0)
    l1.setProperty("start_point", [0, 0, 0])
    l1.setProperty("end_point", [5, 0, 0])
    l1.compile()

    c1 = CircleScenario(10.0, 20.0)
    c1.setProperty("center_point", [5, 3, 5])
    c1.setProperty("start_point", [5, 0, 0])
    c1.compile()

    s = l1 + c1
    s.addNode(node1, 0.0)
    s.addNode(node2, 0.5)
    s.addNode(node3, 1.0)
    s.run()

    output.outputXML("./result.sc", [node1,node2,node3])

    util.showScenarioTrajectory(s)

def triangleScenarioTest() :

    node1 = Node(1, 'n1')
    node2 = Node(2, 'n2')
    node3 = Node(3, 'n3')
    node4 = Node(4, 'n4')
    node5 = Node(5, 'n5')
    node6 = Node(6, 'n6')
    node7 = Node(7, 'n7')
    node8 = Node(8, 'n8')
    node9 = Node(9, 'n9')
    node10 = Node(10, 'n10')

    node1.initPosition(0, 0, 0)
    node2.initPosition(3, 0, 0)
    node3.initPosition(6, 0, 0)
    node4.initPosition(9, 0, 0)

    node5.initPosition(1.5, 3, 0)
    node6.initPosition(4.5, 3, 0)
    node7.initPosition(7.5, 3, 0)

    node8.initPosition(3, 6, 0)
    node9.initPosition(6, 6, 0)

    node10.initPosition(4.5, 9, 0)


    group1 = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10]

    ## S1 Scenario
    s1 = IScenario(0, 10)
    s1.setProperty('trans', [0.0, 0.0, 4.0])
    s1.setProperty('is_moving', False)
    s1.addNode(group1)
    s1.changeColor(0.0, [0,0,255, 0, 0,200])
    s1.compile()
    s1.run()

    ## S2 Scenario
    s2 = IScenario(10, 20)
    center_pos = (np.array(node2.lastPos()) + np.array(node3.lastPos())) / 2
    s2.setProperty("rot_center", center_pos)
    s2.setProperty("rot_angle", 90)
    s2.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s2.setProperty('is_moving', False)
    s2.addNode(group1)
    s2.changeColor(10.0, [0,0,0, 255, 0,200])
    s2.compile()
    s2.run()

    ## S3 Scenario
    s3 = IScenario(20, 30)
    center_pos = (np.array(node2.lastPos()) + np.array(node3.lastPos())) / 2
    s3.setProperty("rot_center", center_pos)
    s3.setProperty("rot_angle", 360)
    s3.setProperty("rot_direct", [0.0, 0.0, 1.0])
    s3.setProperty('is_moving', False)
    s3.addNode(group1)
    s3.changeColor(20.0, [0,0,0, 0, 255,200])
    s3.compile()
    s3.run()

    ## S4 Scenario
    s4 = IScenario(40, 50)
    center_pos = (np.array(node2.lastPos()) + np.array(node3.lastPos())) / 2
    s4.setProperty("rot_center", center_pos)
    s4.setProperty("rot_angle", -90)
    s4.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s4.setProperty('is_moving', False)
    s4.addNode(group1)
    s4.changeColor(40.0, [0,0,255,255,0,200])
    s4.compile()
    s4.run()

    ## S5 Scenario
    s5 = IScenario(50, 60)
    s5.setProperty('trans', [0.0, 0.0, -4.0])
    s5.setProperty('is_moving', False)
    s5.addNode(group1)
    s4.changeColor(50.0, [0,0,255,255,255,200])
    s5.compile()
    s5.run()

    output.outputXML("./result.sc", group1)

    #util.showScenarioTrajectory(s1)
    #util.showScenarioTrajectory(s2)
    #util.showScenarioTrajectory(s3)
    util.showNodeTrajectory([node1, node2, node3, node4, node5, node6, node7, node8, node9, node10])

def rectScenario() :

    nodes = []
    for i in range(20) :
        x = (i%5)*3.0
        y = int(i/5)*3.0
        node = Node(i+1)
        node.initPosition(x,y,0)
        nodes.append(node)

    ## Takeoff
    for n in nodes[0:5]:
        n.setProperty('takeoff_time', 5.0)

    for n in nodes[5:10]:
        n.setProperty('takeoff_time', 10.0)

    for n in nodes[10:15]:
        n.setProperty('takeoff_time', 15.0)

    for n in nodes[15:20]:
        n.setProperty('takeoff_time', 20.0)


    ## S1 Scenario
    start_time, end_time = util.nextScenTime(25.0, 10)
    s1 = IScenario(start_time, end_time)
    s1.setProperty('trans', [0.0, 0.0, 2.5])
    s1.setProperty('is_moving', False)
    s1.addNode(nodes)
    s1.compile()
    s1.run()
    s1.changeColor(25, [0,0,0,0,0,0])

    ## S2 Scenario
    start_time, end_time = util.nextScenTime(end_time, 20)
    s2 = IScenario(start_time, end_time)
    center_pos = nodes[2].lastPos()
    s2.setProperty("rot_center", center_pos)
    s2.setProperty("rot_angle", 40)
    s2.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s2.setProperty('is_moving', False)
    s2.addNode(nodes)
    s2.changeColor(35.0, [0,0,255,255,255,230])
    s2.compile()
    s2.run()

    ## S3 Scenario
    start_time, end_time = util.nextScenTime(end_time+5, 40)
    s3 = IScenario(start_time, end_time)
    center_pos = (np.array(nodes[7].lastPos()) + np.array(nodes[12].lastPos())) / 2

    s3.setProperty("rot_center", center_pos)
    s3.setProperty("rot_angle", 360)
    s3.setProperty("rot_direct", [0.0, 0.0, 1.0])
    s3.setProperty('is_moving', False)
    s3.addNode(nodes)
    s3.compile()
    s3.run()

    ## Color Change
    for n,i in zip(nodes, range(len(nodes))) :
        n.setColor(55.0 + i * 0.1, [0, 0, 255, 0, 0, 230])

    s3.changeColor(60, [0,0,0,255,0,230])
    s3.changeColor(70, [0,0,0,0,255,230])

    for i in [0,1,2,3,4,5,9,10,14,15,16,17,18,19] :
        nodes[i].setColor(80, [0, 0, 255, 0, 0, 230])

    ## S4 Scenario
    start_time, end_time = util.nextScenTime(end_time+5, 10)
    s4 = IScenario(start_time, end_time)
    center_pos = nodes[2].lastPos()
    s4.setProperty("rot_center", center_pos)
    s4.setProperty("rot_angle", -40)
    s4.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s4.setProperty('is_moving', False)
    s4.addNode(nodes)
    s4.compile()
    s4.run()


    ## S5 Scenario
    start_time, end_time = util.nextScenTime(end_time+5, 10)
    s5 = IScenario(start_time, end_time)
    s5.setProperty('trans', [0.0, 0.0, -2.5])
    s5.setProperty('is_moving', False)
    s5.addNode(nodes)
    s5.compile()
    s5.run()

    ## Landing
    for i in range(20) :
        nodes[i].setLanding(end_time+3)


    output.outputXML("./rect.sc", nodes)

    util.showNodeTrajectory(nodes)

def spiralTest() :

    node1 = Node(1, 'n1')
    node2 = Node(2, 'n2')
    node3 = Node(3, 'n3')

    s = SpiralScenario(0.0, 10.0)
    s.setProperty("start_point", [5, 5, 0])
    s.setProperty("center_point", [5, 0, 0])
    s.setProperty("point_number", 500)
    s.setProperty("height", 10)
    s.setProperty("twist_number", 5)
    s.compile()


    s.addNode(node1, 0.0)
    s.addNode(node2, 0.5)
    s.addNode(node3, 1.0)
    s.run()

    output.outputXML("./result.sc", [node1,node2,node3])

    util.showScenarioTrajectory(s)

def triangle_circleTest() :

    ## S2 Scenario
    node1 = Node(1, 'n1')
    node2 = Node(2, 'n2')
    node3 = Node(3, 'n3')
    node4 = Node(4, 'n4')
    node5 = Node(5, 'n5')
    node6 = Node(6, 'n6')
    node7 = Node(7, 'n7')
    node8 = Node(8, 'n8')
    node9 = Node(9, 'n9')
    node10 = Node(10, 'n10')
    node11 = Node(11, 'n11')
    node12 = Node(12, 'n12')
    node13 = Node(13, 'n13')
    node14 = Node(14, 'n14')
    node15 = Node(15, 'n15')

    temp_x = 0
    temp_y = 0

    node1.initPosition(temp_x, temp_y, 0)
    node2.initPosition(temp_x+3, temp_y, 0)
    node3.initPosition(temp_x+6, temp_y, 0)
    node4.initPosition(temp_x+9, temp_y, 0)
    node5.initPosition(temp_x+12, temp_y, 0)

    node6.initPosition(temp_x +1.5, temp_y+3, 0)
    node7.initPosition(temp_x +4.5, temp_y+3, 0)
    node9.initPosition(temp_x + 7.5, temp_y+3, 0)
    node10.initPosition(temp_x +10.5, temp_y+3, 0)

    node11.initPosition(temp_x+3, temp_y+6, 0)
    node8.initPosition(temp_x+6, temp_y+6, 0)
    node15.initPosition(temp_x+9, temp_y+6, 0)

    node12.initPosition(temp_x + 4.5, temp_y + 9, 0)
    node14.initPosition(temp_x + 7.5, temp_y + 9, 0)

    node13.initPosition(temp_x + 6, temp_y + 12, 0)

    group1 = [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15]

    ## S1 Scenario
    s1 = IScenario(0, 10)
    s1.setProperty('trans', [0.0, 0.0, 4.0])
    s1.setProperty('is_moving', False)
    s1.addNode(group1)
    s1.changeColor(0.0, [0, 0, 255, 0, 0, 200])
    s1.compile()
    s1.run()

    ## S2 Scenario
    s2 = IScenario(10, 20)
    center_pos = (np.array(node3.lastPos()))
    s2.setProperty("rot_center", center_pos)
    s2.setProperty("rot_angle", 90)
    s2.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s2.setProperty('is_moving', False)
    s2.addNode(group1)
    s2.changeColor(10.0, [0, 0, 0, 255, 0, 200])
    s2.compile()
    s2.run()

    ## S3 Scenario
    s3 = IScenario(20, 30)
    center_pos = (np.array(node3.lastPos()))
    s3.setProperty("rot_center", center_pos)
    s3.setProperty("rot_angle", 360)
    s3.setProperty("rot_direct", [0.0, 0.0, 1.0])
    s3.setProperty('is_moving', False)
    s3.addNode(group1)
    s3.changeColor(20.0, [0, 0, 0, 0, 255, 200])
    s3.compile()
    s3.run()

    # # circle Scenario

    node16 = Node(16, 'n16')
    node17 = Node(17, 'n17')
    node18 = Node(18, 'n18')
    node19 = Node(19, 'n19')
    node20 = Node(20, 'n20')

    cir_group1 = [node16, node17, node18, node19, node20]

    c1 = CircleScenario(20, 30.0)
    c1.setProperty("center_point", [temp_x+6, temp_y, 20])
    c1.setProperty("start_point", [temp_x+6, temp_y-4, 20])
    c1.addNode(node16, 0.0)
    c1.addNode(node17, 1.0)
    c1.addNode(node18, 2.0)
    c1.addNode(node19, 3.0)
    c1.addNode(node20, 4.0)
    c1.compile()
    c1.run()
    c1.changeColor(0, [0,0,0,0,0,0])
    #
    # s = s1+s2+s3 + c1
    #
    # s.run()

    #output.outputXML("./result.sc", [node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15,node16,node17,node18,node19,node20])

    util.showNodeTrajectory([node1, node2, node3, node4, node5, node6, node7, node8, node9, node10, node11, node12, node13, node14, node15,node16,node17,node18,node19,node20])


def treeScenario() :
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node6 = Node(6)
    node7 = Node(7)
    node8 = Node(8)
    node9 = Node(9)
    node10 = Node(10)
    node11 = Node(11)
    node12 = Node(12)
    node13 = Node(13)
    node14 = Node(14)
    node15 = Node(15)
    node16 = Node(16)
    node17 = Node(17)
    node18 = Node(18)
    node19 = Node(19)
    node20 = Node(20)

    group = [node1, node2, node3, node4, node5,
             node6, node7, node8, node9, node10,
             node11, node12, node13, node14, node15,
             node16, node17, node18, node19, node20]

    for n, i in zip(group, range(len(group))):
        x = (i % 5) * 3.0
        y = int(i / 5) * 3.0
        n.initPosition(x, y, 0)

    ## Takeoff

    for i in [15,16,17,18,19]:
        group[i].setProperty('takeoff_time', 5.0)
        group[i].setColor(5.0, [0,0,255,255,255,250])

    for i in [10,11,12,13,14]:
        group[i].setProperty('takeoff_time', 8.0)
        group[i].setColor(8.0, [0, 0, 255, 255, 255, 250])

    for i in [5,6,7,8,9]:
        group[i].setProperty('takeoff_time', 11.0)
        group[i].setColor(11.0, [0, 0, 255, 255, 255, 250])

    for i in [0,1,2,3,4]:
        group[i].setProperty('takeoff_time', 14.0)
        group[i].setColor(14.0, [0, 0, 255, 255, 255, 250])

    start_time = 16
    interval = 6
    t1 = start_time + interval*0
    t2 = start_time + interval*1
    t3 = start_time + interval*2
    t4 = start_time + interval*3
    t5 = start_time + interval*4
    t6 = start_time + interval*5
    t7 = start_time + interval*6

    ## Make position
    h = 1.5
    start_time, end_time = util.nextScenTime(t1, interval)
    s18 = IScenario(start_time, end_time)
    s18.setProperty('trans', [0, 7,h])
    s18.setProperty('is_moving', False)
    s18.addNode(node18)
    s18.changeColor(t1, [0,0,0,255,0,250])
    s18.compile()
    s18.run()

    start_time, end_time = util.nextScenTime(t2, interval)
    s17 = IScenario(start_time, end_time)
    s17.setProperty('trans', [1.5, 4, h])
    s17.setProperty('is_moving', False)
    s17.addNode(node17)
    s17.changeColor(t2, [0,0,0,255,0,250])
    s17.compile()
    s17.run()

    start_time, end_time = util.nextScenTime(t2, interval)
    s19 = IScenario(start_time, end_time)
    s19.setProperty('trans', [-1.5, 4, h])
    s19.setProperty('is_moving', False)
    s19.addNode(node19)
    s19.changeColor(t2, [0,0,0,255,0,250])
    s19.compile()
    s19.run()

    start_time, end_time = util.nextScenTime(t3, interval)
    s16 = IScenario(start_time, end_time)
    s16.setProperty('trans', [3, 1, h])
    s16.setProperty('is_moving', False)
    s16.addNode(node16)
    s16.changeColor(t3, [0,0,0,255,0,250])
    s16.compile()
    s16.run()

    start_time, end_time = util.nextScenTime(t3, interval)
    s13 = IScenario(start_time, end_time)
    s13.setProperty('trans', [0, 4, h])
    s13.setProperty('is_moving', False)
    s13.addNode(node13)
    s13.changeColor(t3, [0,0,0,255,0,250])
    s13.compile()
    s13.run()

    start_time, end_time = util.nextScenTime(t3, interval)
    s20 = IScenario(start_time, end_time)
    s20.setProperty('trans', [-3, 1, h])
    s20.setProperty('is_moving', False)
    s20.addNode(node20)
    s20.changeColor(t3, [0,0,0,255,0,250])
    s20.compile()
    s20.run()

    start_time, end_time = util.nextScenTime(t4, interval)
    s11 = IScenario(start_time, end_time)
    s11.setProperty('trans', [1.5, 1, h])
    s11.setProperty('is_moving', False)
    s11.addNode(node11)
    s11.changeColor(t4, [0,0,0,255,0,250])
    s11.compile()
    s11.run()

    start_time, end_time = util.nextScenTime(t4, interval)
    s12 = IScenario(start_time, end_time)
    s12.setProperty('trans', [1.5, 1, h])
    s12.setProperty('is_moving', False)
    s12.addNode(node12)
    s12.changeColor(t4, [0,0,0,255,0,250])
    s12.compile()
    s12.run()

    start_time, end_time = util.nextScenTime(t4, interval)
    s14 = IScenario(start_time, end_time)
    s14.setProperty('trans', [-1.5, 1, h])
    s14.setProperty('is_moving', False)
    s14.addNode(node14)
    s14.changeColor(t4, [0,0,0,255,0,250])
    s14.compile()
    s14.run()

    start_time, end_time = util.nextScenTime(t4, interval)
    s15 = IScenario(start_time, end_time)
    s15.setProperty('trans', [-1.5, 1, h])
    s15.setProperty('is_moving', False)
    s15.addNode(node15)
    s15.changeColor(t4, [0,0,0,255,0,250])
    s15.compile()
    s15.run()

    start_time, end_time = util.nextScenTime(t5, interval)
    s6 = IScenario(start_time, end_time)
    s6.setProperty('trans', [0, 1, h])
    s6.setProperty('is_moving', False)
    s6.addNode(node6)
    s6.changeColor(t5, [0,0,0,255,0,250])
    s6.compile()
    s6.run()

    start_time, end_time = util.nextScenTime(t5, interval)
    s7 = IScenario(start_time, end_time)
    s7.setProperty('trans', [0, 1, h])
    s7.setProperty('is_moving', False)
    s7.addNode(node7)
    s7.changeColor(t5, [0,0,0,255,0,250])
    s7.compile()
    s7.run()

    start_time, end_time = util.nextScenTime(t5, interval)
    s8 = IScenario(start_time, end_time)
    s8.setProperty('trans', [0, 1, h])
    s8.setProperty('is_moving', False)
    s8.addNode(node8)
    s8.changeColor(t5, [0,0,0,255,0,250])
    s8.compile()
    s8.run()

    start_time, end_time = util.nextScenTime(t5, interval)
    s9 = IScenario(start_time, end_time)
    s9.setProperty('trans', [0, 1,h])
    s9.setProperty('is_moving', False)
    s9.addNode(node9)
    s9.changeColor(t5, [0,0,0,255,0,250])
    s9.compile()
    s9.run()

    start_time, end_time = util.nextScenTime(t5, interval)
    s10 = IScenario(start_time, end_time)
    s10.setProperty('trans', [0, 1, h])
    s10.setProperty('is_moving', False)
    s10.addNode(node10)
    s10.changeColor(t5, [0,0,0,255,0,250])
    s10.compile()
    s10.run()

    start_time, end_time = util.nextScenTime(t7, interval)
    s1 = IScenario(start_time, end_time)
    s1.setProperty('trans', [3, -1, h])
    s1.setProperty('is_moving', False)
    s1.addNode(node1)
    s1.changeColor(t6, [0,0,255,0,0,250])
    s1.compile()
    s1.run()

    start_time, end_time = util.nextScenTime(t6, interval)
    s2 = IScenario(start_time, end_time)
    s2.setProperty('trans', [1, 1.5, h])
    s2.setProperty('is_moving', False)
    s2.addNode(node2)
    s2.changeColor(t6, [0,0,255,0,0,250])
    s2.compile()
    s2.run()

    start_time, end_time = util.nextScenTime(t7, interval)
    s3 = IScenario(start_time, end_time)
    s3.setProperty('trans', [0, -1,h])
    s3.setProperty('is_moving', False)
    s3.addNode(node3)
    s3.changeColor(t6, [0,0,255,0,0,250])
    s3.compile()
    s3.run()

    start_time, end_time = util.nextScenTime(t6, interval)
    s4 = IScenario(start_time, end_time)
    s4.setProperty('trans', [-1, 1.5, h])
    s4.setProperty('is_moving', False)
    s4.addNode(node4)
    s4.changeColor(t6, [0,0,255,0,0,250])
    s4.compile()
    s4.run()

    start_time, end_time = util.nextScenTime(t7, interval)
    s5 = IScenario(start_time, end_time)
    s5.setProperty('trans', [-3, -1, h])
    s5.setProperty('is_moving', False)
    s5.addNode(node5)
    s5.changeColor(t6, [0,0,255,0,0,250])
    s5.compile()
    s5.run()

    ## S_up Scenario ##
    start_time, end_time = util.nextScenTime(end_time+3, 30)
    s_up = IScenario(start_time, end_time)
    center_pos = (np.array(node3.lastPos()))
    s_up.setProperty("rot_center", center_pos)
    s_up.setProperty("rot_angle", 90)
    s_up.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s_up.setProperty('is_moving', False)
    s_up.addNode(group)
    for i in range(5):
        group[i].setColor(start_time+5, [0,0,100,60,0,250])
    for i in range(5, 20):
        group[i].setColor(start_time+5, [0,0,212,244,250,250])

    s_up.compile()
    s_up.run()

    ## S_rot Scenario
    start_time, end_time = util.nextScenTime(end_time+5, 50)
    s_rot = IScenario(start_time, end_time)
    center_pos = (np.array(node3.lastPos()))
    s_rot.setProperty("rot_center", center_pos)
    s_rot.setProperty("rot_angle", 360)
    s_rot.setProperty("rot_direct", [0.0, 0.0, 1.0])
    s_rot.setProperty('is_moving', False)
    s_rot.addNode(group)
    for i in [1, 2, 3, 4, 5]:
        group[i - 1].setColor(start_time+10, [0,0,110,20,0,250])
    for i in [6, 8, 10, 12, 15, 16, 18, 19, 20]:
        group[i - 1].setColor(start_time+10, [0,0,0,150,0,250])
    for i in [7, 9, 11, 13, 14, 17]:
        group[i - 1].setColor(start_time+10, [0,0,255,255,50,250])

    group[17].setColor(start_time+10, [0x16, 0, 255, 0, 0, 250])
    group[17].setColor(start_time+15, [0x16, 0, 255, 255, 255, 250])

    for i in [1, 2, 3, 4, 5]:
        group[i - 1].setColor(start_time + 20, [0, 0, 30, 220, 20, 250])
    for i in [6, 8, 10, 12, 15, 16, 18, 19, 20]:
        group[i - 1].setColor(start_time + 20, [0,0,255,0,0,250])
    for i in [7, 9, 11, 13, 14, 17]:
        group[i - 1].setColor(start_time + 20, [0,0,0,210,255,250])

    group[17].setColor(start_time + 20, [0x16, 0, 255, 255, 255, 250])

    for i in [17,18,19,14,9,8,7,6,5,10,15,16]:
        group[i ].setColor(start_time + 30, [0,0,0,255,90,250])
    for i in [11,12,13]:
        group[i ].setColor(start_time + 30, [0,0,216,255,0,250])
    for i in [1, 2, 3, 4, 5]:
        group[i - 1].setColor(start_time + 30, [0,0,228,0,225,250])


    for i in [17,18,19,14,9,8,7,6,5,10,15,16]:
        group[i].setColor(start_time + 35, [0x16,0,50,150,40,250])
    for i in [11,12,13]:
        group[i].setColor(start_time + 35, [0x16,0,0,255,90,250])
    for i in [1, 2, 3, 4, 5]:
        group[i -1].setColor(start_time + 35, [0x16,0,150,50,0,250])

    s_rot.compile()
    s_rot.run()

    start_time, end_time = util.nextScenTime(end_time+5, 30)
    s_down = IScenario(start_time, end_time)
    center_pos = (np.array(node3.lastPos()))
    s_down.setProperty("rot_center", center_pos)
    s_down.setProperty("rot_angle", -90)
    s_down.setProperty("rot_direct", [1.0, 0.0, 0.0])
    s_down.setProperty('is_moving', False)
    s_down.addNode(group)
    for i in range(5):
        group[i].setColor(start_time, [0,0,0,155,200,250])
    for i in range(15):
        group[i+5].setColor(start_time, [0,0,255,0,0,250])

    s_down.compile()
    s_down.run()

    start_time, end_time = util.nextScenTime(end_time+2, 5)
    down_land = IScenario(start_time, end_time)
    down_land.setProperty('trans', [0, 0, -2.0])
    down_land.setProperty('is_moving', False)
    down_land.addNode(group)
    down_land.changeColor(start_time, [0,0,200,200,200,250])
    down_land.changeColor(start_time+4, [0, 0, 0, 0, 0, 0])
    down_land.compile()
    down_land.run()

    ## Landing
    for i in range(20):
        group[i].setLanding(end_time + 5)

    ## output
    output.outputXML("./tree.sc", group)

    # util.showNodeTrajectory([node1,node2])
    util.showNodeTrajectory(group)


if __name__ == "__main__":
    # linecircleTest()
    # triangleScenarioTest()
    #rectScenario()
    # spiralTest()
    # triangle_circleTest()
    #  treeScenario()
    takeoffTest()
