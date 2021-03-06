#####################################
# Taegeuk Scenario 
# - # of drone : 30
#####################################

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


def transScen(start_time, end_time, nodes, dst_pos):
    for n in nodes:
        nid = n.id()
        s1 = IScenario(start_time, end_time)
        s1.setProperty('is_moving', False)
        delta = np.array(dst_pos[nid]) - np.array(n.lastPos())
        s1.setProperty('trans', delta.tolist())
        s1.addNode(n)
        s1.compile()
        s1.run()


def changeColor(start_time, end_time, nodes, color):
    for n in nodes:
        n.setColor(start_time, color)


def test1Scenario():
    red = [0, 0, 255, 0, 0, 255]
    green = [0, 0, 0, 255, 0, 255]
    blue = [0, 0, 0, 0, 255, 255]
    brown = [0, 0, 0, 150, 50, 255]

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
    node21 = Node(21)
    node22 = Node(22)
    node23 = Node(23)
    node24 = Node(24)
    node25 = Node(25)
    node26 = Node(26)
    node27 = Node(27)
    node28 = Node(28)
    node29 = Node(29)
    node30 = Node(30)

    group = [node1, node2, node3, node4, node5,
             node6, node7, node8, node9, node10,
             node11, node12, node13, node14, node15,
             node16, node17, node18, node19, node20, node21, node22, node23, node24, node25, node26, node27, node28,
             node29, node30]

    init_pos = {}  ## initial position
    for n, i in zip(group, range(len(group))):
        x = (i % 5) * 2.0
        y = int(i / 5) * 2.0
        n.initPosition(x, y, 0)
        init_pos[n.id()] = n.lastPos()

    ## Takeoff
    for i in [1, 2, 3, 4, 5, 11, 12, 13, 14, 15, 21, 22, 23, 24, 25]:
        group[i - 1].setProperty('takeoff_time', 4.0)

    for i in [6, 7, 8, 9, 10, 16, 17, 18, 19, 20, 26, 27, 28, 29, 30]:
        group[i - 1].setProperty('takeoff_time', 2.0)

    ###########################################################################
    # TAEGEUK SCEN
    ###########################################################################


    l1_dis=15
    l2_dis=14
    l3_dis=13
    l4_dis=12

    taeguek_pos = {}
    taeguek_pos[21] = [2, l1_dis, 3]  ## 1
    taeguek_pos[22] = [4.75, l1_dis, 1.25]  ## 3
    taeguek_pos[23] = [6.75, l1_dis, 4.75]  ## 13
    taeguek_pos[24] = [8.6, l1_dis, 1.75]  ## 5
    taeguek_pos[25] = [10.75, l1_dis, 5.1]  ## 15
    taeguek_pos[26] = [1.1, l1_dis, 6.8]  ## 11
    taeguek_pos[27] = [3.25, l1_dis, 10.25]  ## 21
    taeguek_pos[28] = [5.25, l1_dis, 7.25]  ## 18\
    taeguek_pos[29] = [7, l1_dis, 10.75]  ## 27
    taeguek_pos[30] = [9.75, l1_dis, 9]  ## 30

    taeguek_pos[12] = [3.0, l2_dis, 1.8]  ## 2
    taeguek_pos[14] = [6.75, l2_dis, 1]  ## 4
    taeguek_pos[11] = [1.25, l2_dis, 4.75]  ## 6
    taeguek_pos[15] = [10, l2_dis, 3.25]  ## 10
    taeguek_pos[13] = [4.75, l2_dis, 5.25]  ## 12
    taeguek_pos[16] = [1.9, l2_dis, 8.75]  ## 16
    taeguek_pos[18] = [7.2, l2_dis, 6.75]  ## 19
    taeguek_pos[20] = [10.6, l2_dis, 7.25]  ## 25
    taeguek_pos[17] = [5.2, l2_dis, 10.75]  ## 26
    taeguek_pos[19] = [8.5, l2_dis, 10]  ## 28

    taeguek_pos[6] = [3.25, l3_dis, 4]  ## 7
    taeguek_pos[9] = [7, l3_dis, 2.75]  ## 9
    taeguek_pos[10] = [9, l3_dis, 5.9]  ## 20
    taeguek_pos[7] = [3.6, l3_dis, 8]  ## 22
    taeguek_pos[8] = [7.0, l3_dis, 9.0]  ## 29

    taeguek_pos[3] = [5.25, l4_dis, 3]  ## 8
    taeguek_pos[4] = [8.5, l4_dis, 4]  ## 14
    taeguek_pos[1] = [3, l4_dis, 6]  ## 17
    taeguek_pos[2] = [4.75, l4_dis, 9.25]  ## 23
    taeguek_pos[5] = [8.75, l4_dis, 8]  ## 24

    start_time = 6
    g1_t1 = start_time + 1
    g1_dt1 = 10
    c_change_dt = 24
    changeColor(start_time, 3, group, [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(g1_t1, g1_dt1)
    transScen(start_time, end_time, [node26, node27, node28, node29, node30], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node26, node27, node28, node29, node30], [0, 0, 255, 0, 0, 255])

    start_time, end_time = util.nextScenTime(end_time - 7, g1_dt1)
    transScen(start_time, end_time, [node21, node22, node23, node24, node25], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node21, node22, node23, node24, node25], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time - 6, g1_dt1)
    transScen(start_time, end_time, [node16, node17, node18, node19, node20], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node16, node17, node19], [0, 0, 255, 0, 0, 255])
    changeColor(g1_t1 + c_change_dt, end_time, [node18, node20], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time - 7, g1_dt1)
    transScen(start_time, end_time, [node11, node12, node13, node14, node15], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node11, node13], [0, 0, 255, 0, 0, 255])
    changeColor(g1_t1 + c_change_dt, end_time, [node12, node14, node15], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time - 7, g1_dt1)
    transScen(start_time, end_time, [node6, node7, node8, node9, node10], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node6, node7, node8], [0, 0, 255, 0, 0, 255])
    changeColor(g1_t1 + c_change_dt, end_time, [node9, node10], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time - 7, g1_dt1)
    transScen(start_time, end_time, [node1, node2, node3, node4, node5], taeguek_pos)
    changeColor(g1_t1 + c_change_dt, end_time, [node1, node2], [0, 0, 255, 0, 0, 255])
    changeColor(g1_t1 + c_change_dt, end_time, [node3, node4, node5], [0, 0, 0, 0, 255, 255])

    ###########################################################################
    # TAEGEUK ROTATION
    ###########################################################################

    t_rot = end_time
    g1_dt2 = 40
    center1 = [6, l1_dis, 6]
    group1 = [node29,node19,node30,node20,node25,
              node15,node24,node14,node22,node12,
              node21,node11,node26,node16,node27,
              node17]

    start_time, end_time = util.nextScenTime(end_time +2, g1_dt2)
    s_rot1 = IScenario(start_time, end_time)
    s_rot1.setProperty("rot_center", center1)
    s_rot1.setProperty("rot_angle", 360)
    s_rot1.setProperty("rot_direct", [0.0, 1.0, 0.0])
    s_rot1.setProperty('is_moving', False)
    s_rot1.addNode(group1)
    s_rot1.compile()
    s_rot1.run()


    duration = end_time - start_time
    for t in np.arange(start_time, end_time, 0.1) :
        for n,i in zip(group1, range(len(group1))) :
            offset = 10 
            RED2BLUE = 50 
            BLUE2RED = 250 
            angle = (i*(360.0/len(group1)) + (360.0/(duration)) * (t-start_time) + offset )%360

            if (angle >= 0 and angle <= RED2BLUE-5) or (angle >= BLUE2RED+5 and angle <= 360) :
                changeColor(t, 0, [n], red)
            elif (angle >= RED2BLUE+5) and (angle <= BLUE2RED-5) :
                changeColor(t, 0, [n], blue)
            elif (angle >= RED2BLUE-5) and (angle <= RED2BLUE+5) : # red -> blue
                ratio = (RED2BLUE+5 - angle)  / 10.0
                changeColor(t, 0, [n], [0, 0, int(255.0*ratio), 0, int(255.0*(1.0-ratio)), 255])
            elif (angle >= BLUE2RED-5) and (angle <= BLUE2RED+5) : # blue -> red
                ratio = (BLUE2RED+5 - angle)  / 10.0
                changeColor(t, 0, [n], [0, 0, int(255.0*(1.0-ratio)), 0, int(255.0*ratio), 255])

    ###########################################################################
    # SARAM-IN SCEN 
    ###########################################################################
    '''
    l1_dis = 7.6
    l2_dis = 8.8
    l3_dis = 10
    l4_dis = 10

    in_pos = {}
    in_pos[1] = [0.75, l1_dis, 1.25]
    in_pos[2] = [4.75, l1_dis, 7.7]
    in_pos[3] = [3, l1_dis, 4.1]
    in_pos[4] = [8.7, l1_dis, 2.2]
    in_pos[5] = [6.25, l1_dis, 4.6]
    in_pos[6] = [1.75, l1_dis, 2.6]
    in_pos[7] = [4, l1_dis, 5.75]
    in_pos[8] = [4.6, l1_dis, 9.2]
    in_pos[9] = [7.6, l1_dis, 3.4]
    in_pos[10] = [9.75, l1_dis, 1.2]


    in_pos[11] = [2.25, l2_dis, 1.4]
    in_pos[12] = [4.25, l2_dis, 4.25]
    in_pos[13] = [5.25, l2_dis, 5.75]
    in_pos[14] = [7.5, l2_dis, 4.75]
    in_pos[15] = [11.25, l2_dis, 1]
    in_pos[16] = [3.25, l2_dis, 2.6]
    in_pos[17] = [5.9, l2_dis, 8.5]
    in_pos[18] = [6.25, l2_dis, 6.75]
    in_pos[19] = [8.75, l2_dis, 3.5]
    in_pos[20] = [10, l2_dis, 2.25]


    in_pos[21] = [1.6, l3_dis, 1.6]
    in_pos[22] = [3.0, l3_dis, 3.25]
    in_pos[23] = [7.5, l3_dis, 4]
    in_pos[24] = [9, l3_dis, 2.5]
    in_pos[25] = [10.25, l3_dis, 1.3]
    in_pos[26] = [4, l3_dis, 4.8]
    in_pos[27] = [5.2, l3_dis, 9]
    in_pos[28] = [4.75, l3_dis, 6.25]
    in_pos[29] = [5.5, l3_dis, 7.75]
    in_pos[30] = [6.4, l3_dis, 5.5]


    # g1_t2 = t_rot + g1_dt2 +3
    g1_t2 = end_time + 3
    g1_dt3 = 10

    start_time, end_time = util.nextScenTime(g1_t2, g1_dt3)
    transScen(start_time, end_time, [node1, node2, node3, node4, node5], in_pos)
    changeColor(start_time, end_time, [node1, node2, node3, node4, node5], brown)

    start_time, end_time = util.nextScenTime(end_time, g1_dt3)
    transScen(start_time, end_time, [node6, node7, node8, node9, node10], in_pos)
    changeColor(start_time, end_time, [node6, node7, node8, node9, node10], brown)

    start_time, end_time = util.nextScenTime(end_time, g1_dt3)
    transScen(start_time, end_time, [node11, node12, node13, node14, node15], in_pos)
    changeColor(start_time, end_time, [node11, node12, node13, node14, node15], brown)

    start_time, end_time = util.nextScenTime(end_time, g1_dt3)
    transScen(start_time, end_time, [node16, node17, node18, node19, node20], in_pos)
    changeColor(start_time, end_time, [node16, node17, node18, node19, node20], brown)

    start_time, end_time = util.nextScenTime(end_time, g1_dt3)
    transScen(start_time, end_time, [node21, node22, node23, node24, node25], in_pos)
    changeColor(start_time, end_time, [node21, node22, node23, node24, node25], brown)

    start_time, end_time = util.nextScenTime(end_time, g1_dt3)
    transScen(start_time, end_time, [node26, node27, node28, node29, node30], in_pos)
    changeColor(start_time, end_time, [node26, node27, node28, node29, node30], brown)
    '''
    ####################################################################################################################
    ## Come back to initial position
    end_time = end_time  + 10

    start_time, end_time = util.nextScenTime(end_time, g1_dt1)
    transScen(start_time, end_time, [node1, node2, node3, node4, node5], init_pos)

    start_time, end_time = util.nextScenTime(end_time - 3, g1_dt1)
    transScen(start_time, end_time, [node6, node7, node8, node9, node10], init_pos)

    start_time, end_time = util.nextScenTime(end_time - 3, g1_dt1)
    transScen(start_time, end_time, [node11, node12, node13, node14, node15], init_pos)

    start_time, end_time = util.nextScenTime(end_time - 3, g1_dt1)
    transScen(start_time, end_time, [node16, node17, node18, node19, node20], init_pos)

    start_time, end_time = util.nextScenTime(end_time - 3, g1_dt1)
    transScen(start_time, end_time, [node21, node22, node23, node24, node25], init_pos)

    start_time, end_time = util.nextScenTime(end_time - 3, g1_dt1)
    transScen(start_time, end_time, [node26, node27, node28, node29, node30], init_pos)

    ## Landing
    for i in range(30):
        group[i - 1].setLanding(end_time + 10)

    ## output
    output.outputXML("./test_taegeuk.sc", group)

    ## check speed
    util.checkSpeed(group)
    #util.checkDist(group)

    ## show node trajecotry using animation
    util.showNodeTrajectory(group)


if __name__ == "__main__":
    test1Scenario()
