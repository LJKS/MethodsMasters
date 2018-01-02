import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = GridWorld(path)

    def create_policy(self):
        #TODO
        directions = GridWorld.getSize(self.world)
        print(directions)


    def evaluate_policy(self):
        #TODO
        a=5
    def iterate_policy(self):
        #TODO
        a=5
    def print_solutions(self):
        #TODO
        a=5
hallo = mdp('3by4.grid')
hallo.create_policy()
