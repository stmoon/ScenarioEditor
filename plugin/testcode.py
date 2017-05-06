from linescenario import *
import scenario

## TEST LineScenario ##
line = LineScenario(10.1,20.2)
line.addNode('node1')
line.setProperty('start_point', [5,0,0])
line.setProperty('end_point', [10,10,10])
line.setProperty('rate', 10)
line.update()

result = line.trajectory('node1')
print result


