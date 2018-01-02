import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = GridWorld(path)

    def create_policy(self):
        #TODO
        directions = GridWorld.directions(self.world)


    def evaluate_policy(self):
        #TODO

    def iterate_policy(self):
        #TODO

    def print_solutions(self):
        #TODO

hallo = mdp('3by4.grid')
