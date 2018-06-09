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


def transScen(start_time, end_time, nodes, dst_pos) :
    for n in nodes :
        nid = n.id()
        s1 = IScenario(start_time, end_time)
        s1.setProperty('is_moving', False)
        delta = np.array(dst_pos[nid]) - np.array(n.lastPos())
        s1.setProperty('trans', delta.tolist())    
        s1.addNode(n)
        s1.compile()
        s1.run()


def test1Scenario() :

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
             node16, node17, node18, node19, node20,node21,node22,node23,node24,node25,node26,node27,node28,node29,node30]

    group1 = [node1,node3,node5,node11,node13,node15,node18,node21,node27,node30]
    group2 = [node2, node4, node6, node10, node12, node16, node19, node25,node26,  node28]
    group3 = [node7, node9, node20, node22, node29]
    group4 = [node8, node14, node17, node23, node24]

    for n, i in zip(group, range(len(group))):
        x = (i % 5) * 2.0
        y = int(i / 5) * 2.0
        n.initPosition(x, y, 0)

    ## Takeoff
    for i in [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]:
        group[i-1].setProperty('takeoff_time', 1.0)


    for i in [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]:
        group[i-1].setProperty('takeoff_time', 2.0)


    start_time = 2
    t0 = start_time + 1
    dt0 =1
    t1 = t0+1
    dt1= 5


    h = 0
    start_time, end_time = util.nextScenTime(t0, dt0)
    s_up1 = IScenario(start_time, end_time)
    s_up1.setProperty('trans', [0.0, 0.0, h])
    s_up1.setProperty('is_moving', False)
    s_up1.addNode(group)
    s_up1.changeColor(t0, [0, 0, 0, 0, 0, 0])
    s_up1.compile()
    s_up1.run()


   # s_rot1.setProperty("rot_center", [last_pos_xy[0] / 2, last_pos_xy[0] / 2, last_pos_z[2]])


    ## Make position

    st1= 3
    dst1= 3
    st2 = 6
    dst2= 3
    st3 = 9




    center_z = 3
    last_pos_xyz = node1.lastPos()
    h=1.5
    g1_t1 =  start_time  +1


    ## Translation 
    dst_pos = {}
    dst_pos[21] = [2,15,3]            ## 1
    dst_pos[22] = [4.75,15,1.25]        ## 3
    dst_pos[23] = [6.75,15,4.75]     ## 13
    dst_pos[24] = [8.6,15,1.75]     ## 5
    dst_pos[25] = [10.75,15,5.1]     ## 15
    dst_pos[26] = [1.1,15,6.8]       ## 11
    dst_pos[27] = [3.25,15,10.25]    ## 21
    dst_pos[28] = [5.25,15,7.25]     ## 18
    dst_pos[29] = [7,15,10.75]       ## 27
    dst_pos[30] = [9.75,15,9]        ## 30

    dst_pos[16] = [1.9, 14, 8.75]       ## 16
    dst_pos[17] = [5.2, 14, 10.75]       ##26
    dst_pos[18] = [7.2, 14, 6.75]       ## 19
    dst_pos[19] = [8.5, 14, 10]       ## 28
    dst_pos[20] = [10.6, 14, 7.25]       ## 25
    dst_pos[11] = [1.25, 14, 4.75]       ## 6
    dst_pos[12] = [3.5, 14, 1.8]       ## 2
    dst_pos[13] = [4.75, 14, 5.25]       ## 12
    dst_pos[14] = [6.75, 14, 1]       ## 4
    dst_pos[15] = [10.75, 14, 5.1]       ## 10

    dst_pos[6] = [3.25, 13, 4]       ## 7
    dst_pos[7] = [3.6, 13, 8]       ## 22
    dst_pos[8] = [6.6, 13, 9.0]       ## 29
    dst_pos[9] = [7, 13, 2.75]       ## 9
    dst_pos[10] = [9, 13, 5.9]       ## 20

    dst_pos[1] = [3, 12, 6]       ## 17
    dst_pos[2] = [4.75, 12, 9.25]       ## 23
    dst_pos[3] = [5.25, 12, 2.75]       ## 8
    dst_pos[4] = [8.5, 12, 4]       ## 14
    dst_pos[5] = [8.75, 12, 8]       ## 24

   
    g1_dt1 = 6

    start_time, end_time = util.nextScenTime(g1_t1, g1_dt1)
    transScen(start_time, end_time, [node26,node27,node28,node29,node30], dst_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node21,node22,node23,node24,node25], dst_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node16,node17,node18,node19,node20], dst_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node11,node12,node13,node14,node15], dst_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node6,node7,node8,node9,node10], dst_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node1,node2,node3,node4,node5], dst_pos)
              
    ## Landing
    for i in range(30):
        group[i-1].setLanding(100)

    ## output
    output.outputXML("./test_taegeuk.sc", group)
   # output.outputXML("./test_distance.sc", group)

    # util.showNodeTrajectory([node1,node2])
    util.showNodeTrajectory(group)


if __name__ == "__main__":
     test1Scenario()
