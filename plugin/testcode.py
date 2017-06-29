import scenario
import output
from linescenario import *
from pointscenario import *
from circlescenario import *
from node import *

## TEST PointScenario ##
def test1() :
    print '----TEST PointScenario-----'
    node1 = Node(1,'n1')
    point = PointScenario(3,4)
    point.addNode(node1)
    point.setProperty('start_point', [1,1,1])
    point.setProperty('end_point', [2,2,2])
    point.update()
    point_result = point.trajectory(node1)
    print point_result
    xml_result = point.scenario(node1)
    print xml_result
    print '---------------------------'


## TEST LineScenario ##
def test2() :
    print '----TEST LineScenario-----'
    node1 = Node(1,'n1')
    line = LineScenario(10.1,20.2)
    line.addNode(node1)
    line.setProperty('start_point', [5,0,0])
    line.setProperty('end_point', [10,10,10])
    line.setProperty('rate', 10)
    line.update()

    line_result = line.trajectory(node1)
    print line_result
    xml_result = line.scenario(node1)
    print xml_result
    print '---------------------------'

## XML Output ##
def test3() :
    node1 = Node(1,'n1')
    node2 = Node(2,'n2')
    point = PointScenario(10.1,12.2)
    point.addNode(node1)
    point.setProperty('start_point', [1,1,1])
    point.setProperty('end_point', [2,2,2])
    point.update()

    line = LineScenario(10.1,12.2)
    line.addNode(node2)
    line.setProperty('start_point', [5,0,0])
    line.setProperty('end_point', [10,10,10])
    line.setProperty('rate', 10)
    line.update()

    output.clear()
    output.addTrajectory(point.trajectory())
    output.addTrajectory(line.trajectory())
    output.printXML()


## Test Circle Scenario ##

def test4() :
    print '----TEST Circle Scenario-----'
    node1 = Node(1,'n1')
    node2 = Node(2,'n2')

    circle = CircleScenario(10.1, 12.2)
    circle.addNode(node1)
    circle.addNode(node2)

    circle.setProperty('start_point', [1,1,1])
    circle.setProperty('radius', 5)
    

    circle.update()

    output.clear()
    output.addTrajectory(circle.trajectory())
    output.printXML()


test4()
