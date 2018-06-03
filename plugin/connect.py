from scenario import *
from linescenario import  *
import numpy as np

def connect_scenario(start_scen, end_scen) :

    start_point = dict()
    end_point = dict()

    for scen in start_scen :
        scen.compile()
        for node in scen.nodes() :
            traj = scen.trajectory(node)
            start_point[node] = traj[-1]

    for scen in end_scen :
        scen.compile()
        for node in scen.nodes() : 
            traj = scen.trajectory(node)
            end_point[node] = traj[0]
            
    
    connScen = ConnScenario(start_point, end_point)

    for k in start_point.keys() :
        if k in end_point : 
            connScen.addNode(k)

    return connScen

class ConnScenario(IScenario) :

    def __init__(self, start_pt, end_pt) :
        IScenario.__init__(self, 0.0, 0.0)

        self.start_pt = start_pt
        self.end_pt = end_pt

    ## This is simple connection scenario. 
    ## We should implement new algorithm which can avoid collision
    def compile(self) :
        for k in self.start_pt.keys():
            if k in self.end_pt:
                start_time = self.start_pt[k][0]
                end_time = self.end_pt[k][0]

                line = LineScenario(start_time, end_time)
                line.addNode(k)
                line.setProperty('start_point', self.start_pt[k][1:])
                line.setProperty('end_point', self.end_pt[k][1:])
                line.setProperty('rate', 10)
                line.compile()

                self._nodes[k] = line.trajectory(k)[1:-1]
