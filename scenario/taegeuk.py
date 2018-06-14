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

def changeColor(start_time, end_time, nodes, color) :
    for n in nodes :
        n.setColor(start_time, color)

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

    init_pos = {}           ## initial position
    for n, i in zip(group, range(len(group))):
        x = (i % 5) * 2.0
        y = int(i / 5) * 2.0
        n.initPosition(x, y, 0)
        init_pos[n.id()] = n.lastPos()

    ## Takeoff
    for i in [1,2,3,4,5,11,12,13,14,15,21,22,23,24,25]:
        group[i-1].setProperty('takeoff_time', 4.0)


    for i in [6,7,8,9,10,16,17,18,19,20,26,27,28,29,30]:
        group[i-1].setProperty('takeoff_time', 2.0)


    ##
    l1_dis=15
    l2_dis=14
    l3_dis=13
    l4_dis=12

    taeguek_pos = {}
    taeguek_pos[21] = [2,l1_dis,3]           ## 1
    taeguek_pos[22] = [4.75,l1_dis,1.25]     ## 3
    taeguek_pos[24] = [8.6,l1_dis,1.75]      ## 5
    taeguek_pos[26] = [1.1,l1_dis,6.8]       ## 11
    taeguek_pos[23] = [6.75,l1_dis,4.75]     ## 13
    taeguek_pos[25] = [10.75,l1_dis,5.1]     ## 15
    taeguek_pos[28] = [5.25,l1_dis,7.25]     ## 18
    taeguek_pos[27] = [3.25,l1_dis,10.25]    ## 21
    taeguek_pos[29] = [7,l1_dis,10.75]       ## 27
    taeguek_pos[30] = [9.75,l1_dis,9]        ## 30

    taeguek_pos[12] = [3.5, l2_dis, 1.8]     ## 2
    taeguek_pos[14] = [6.75, l2_dis, 1]      ## 4
    taeguek_pos[11] = [1.25, l2_dis, 4.75]   ## 6
    taeguek_pos[15] = [10, l2_dis, 3.25]     ## 10
    taeguek_pos[13] = [4.75, l2_dis, 5.25]   ## 12
    taeguek_pos[16] = [1.9, l2_dis, 8.75]    ## 16
    taeguek_pos[18] = [7.2, l2_dis, 6.75]    ## 19
    taeguek_pos[20] = [10.6, l2_dis, 7.25]   ## 25
    taeguek_pos[17] = [5.2, l2_dis, 10.75]   ## 26
    taeguek_pos[19] = [8.5, l2_dis, 10]      ## 28


    taeguek_pos[6] = [3.25, l3_dis, 4]       ## 7
    taeguek_pos[9] = [7, l3_dis, 2.75]       ## 9
    taeguek_pos[10] = [9, l3_dis, 5.9]       ## 20
    taeguek_pos[7] = [3.6, l3_dis, 8]        ## 22
    taeguek_pos[8] = [6.6, l3_dis, 9.0]      ## 29

    taeguek_pos[3] = [5.25, l4_dis, 2.75]    ## 8
    taeguek_pos[4] = [8.5, l4_dis, 4]        ## 14
    taeguek_pos[1] = [3, l4_dis, 6]          ## 17
    taeguek_pos[2] = [4.75, l4_dis, 9.25]    ## 23
    taeguek_pos[5] = [8.75, l4_dis, 8]       ## 24
   
    start_time = 6
    g1_t1 = start_time +1
    g1_dt1 = 10
    
    start_time, end_time = util.nextScenTime(g1_t1, g1_dt1)
    transScen(start_time, end_time, [node26,node27,node28,node29,node30], taeguek_pos)
    changeColor(start_time, end_time, [node26,node27,node28,node29,node30], [0, 0, 255, 0, 0, 255])

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node21,node22,node23,node24,node25], taeguek_pos)
    changeColor(start_time, end_time, [node21,node22,node23,node24,node25], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node16,node17,node18,node19,node20], taeguek_pos)
    changeColor(start_time, end_time, [node16,node17,node19,node20], [0, 0, 255, 0, 0, 255])
    changeColor(start_time, end_time, [node18], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node11,node12,node13,node14,node15], taeguek_pos)
    changeColor(start_time, end_time, [node11, node13], [0, 0, 255, 0, 0, 255])
    changeColor(start_time, end_time, [node12, node14, node15], [0, 0, 0, 0, 255, 255])

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node6,node7,node8,node9,node10], taeguek_pos)
    changeColor(start_time, end_time, [node6, node7, node8], [0, 0, 255, 0, 0, 255])
    changeColor(start_time, end_time, [node9, node10], [0, 0, 0, 0, 255, 255])


    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node1,node2,node3,node4,node5], taeguek_pos)
    changeColor(start_time, end_time, [node1, node2], [0, 0, 255, 0, 0, 255])
    changeColor(start_time, end_time, [node3, node4, node5], [0, 0, 0, 0, 255, 255])

    ####################################################################################################################
    l1_dis = 7
    l2_dis = 8
    l3_dis = 9
    l4_dis = 10

    in_pos = {}
    in_pos[1] = [5.5, l1_dis, 6.75]  ## 17
    in_pos[2] = [5.5, l1_dis, 8]  ## 21
    in_pos[3] = [4.75, l1_dis, 5.25]  ## 8
    in_pos[4] = [8.25, l1_dis, 1.75]  ## 14
    in_pos[5] = [7, l1_dis, 3.5]  ## 18

    in_pos[10] = [9.75, l1_dis, 1.75]  ## 24

    in_pos[6] = [3.75, l2_dis, 3.75]  ## 7
    in_pos[11] = [2.75, l2_dis, 2.5]  ## 9
    in_pos[7] = [5.25, l2_dis, 5.75]  ## 12
    in_pos[9] = [8.25, l2_dis, 2.75]  ## 19
    in_pos[15] = [9.25, l2_dis, 2]  ## 20
    in_pos[8] = [5.5, l2_dis, 7.5]  ## 22
    in_pos[13] = [6.25, l2_dis, 4.5]  ## 29

    in_pos[16] = [1.75, l3_dis, 2]  ## 2
    in_pos[14] = [7.75, l3_dis, 2.5]  ## 4
    in_pos[17] = [3.25, l3_dis, 3]  ## 6
    in_pos[25] = [8.75, l3_dis, 1.75]  ## 10
    in_pos[12] = [4.25, l3_dis, 4.25]  ## 16
    in_pos[20] = [6.75, l3_dis, 4]  ## 25
    in_pos[19] = [5.75, l3_dis, 7.25]  ## 26
    in_pos[18] = [5.75, l3_dis, 5.5]  ## 28

    in_pos[23] = [4.5, l4_dis, 4.75]  ## 1
    in_pos[22] = [3.5, l4_dis, 3.25]  ## 3
    in_pos[24] = [7.5, l4_dis, 3]  ## 30
    in_pos[21] = [2.25, l4_dis, 2.25]  ## 5
    in_pos[29] = [8.75, l4_dis, 2.25]  ## 13
    in_pos[26] = [5.25, l4_dis, 6.25]  ## 11
    in_pos[28] = [6, l4_dis, 5]  ## 27
    in_pos[30] = [10.5, l4_dis, 1.75]  ## 15
    in_pos[27] = [6, l4_dis, 7.75]  ## 23

    #g1_t2 = t_rot + g1_dt2 +3
    g1_t2 = end_time + 3
    g1_dt3 = 10

    start_time, end_time = util.nextScenTime(g1_t2, g1_dt3)
    transScen(start_time, end_time, [node1, node2, node3, node4, node5], in_pos)
    changeColor(start_time, end_time, [node1, node2, node3, node4, node5], [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(end_time , g1_dt3)
    transScen(start_time, end_time, [node6, node7, node8, node9, node10], in_pos)
    changeColor(start_time, end_time, [node6, node7, node8, node9, node10], [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(end_time , g1_dt3)
    transScen(start_time, end_time, [node11, node12, node13, node14, node15], in_pos)
    changeColor(start_time, end_time, [node11, node12, node13, node14, node15], [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(end_time , g1_dt3)
    transScen(start_time, end_time, [node16, node17, node18, node19, node20], in_pos)
    changeColor(start_time, end_time, [node16, node17, node18, node19, node20], [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(end_time , g1_dt3)
    transScen(start_time, end_time, [node21, node22, node23, node24, node25], in_pos)
    changeColor(start_time, end_time, [node21, node22, node23, node24, node25], [0, 0, 0, 255, 0, 255])

    start_time, end_time = util.nextScenTime(end_time , g1_dt3)
    transScen(start_time, end_time, [node26, node27, node28, node29, node30], in_pos)
    changeColor(start_time, end_time, [node26, node27, node28, node29, node30], [0, 0, 0, 255, 0, 255])

    end_time = end_time +g1_dt3 +7
    ####################################################################################################################
    ## Come back to initial position
    end_time = start_time + 20
    
    start_time, end_time = util.nextScenTime(end_time, g1_dt1)
    transScen(start_time, end_time, [node1,node2,node3,node4,node5], init_pos)

 
    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node6,node7,node8,node9,node10], init_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node11,node12,node13,node14,node15], init_pos)
             
    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node16,node17,node18,node19,node20], init_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node21,node22,node23,node24,node25], init_pos)

    start_time, end_time = util.nextScenTime(end_time-3, g1_dt1)
    transScen(start_time, end_time, [node26,node27,node28,node29,node30], init_pos)

    ## Landing
    for i in range(30):
        group[i-1].setLanding(end_time+10)

    ## output
    output.outputXML("./test_taegeuk.sc", group)

    ## check speed
    #util.checkSpeed(group)
    util.checkDist(group)

    ## show node trajecotry using animation
    util.showNodeTrajectory(group)


if __name__ == "__main__":
     test1Scenario()
