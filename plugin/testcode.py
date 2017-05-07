import scenario

from linescenario import *
from pointscenario import *


## TEST PointScenario ##
print '----TEST PointScenario-----'
point = PointScenario(3,4)
point.addNode('node1')
point.setProperty('start_point', [1,1,1])
point.setProperty('end_point', [2,2,2])
point.update()
point_result = point.trajectory('node1')

print point_result
print '---------------------------'

## TEST LineScenario ##
print '----TEST LineScenario-----'
line = LineScenario(10.1,20.2)
line.addNode('node1')
line.setProperty('start_point', [5,0,0])
line.setProperty('end_point', [10,10,10])
line.setProperty('rate', 10)
line.update()

line_result = line.trajectory('node1')
print line_result
print '---------------------------'

