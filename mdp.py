import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = GridWorld(path)
        self.directions = self.world.get_directions()
    def create_policy(self):
        #TODO
        directionsTranslator = {0:'u', 1: 'd', 2: 'l', 3: 'r'}
        policy = np.random.randint(0,len(self.directions),self.world.get_size())
        outPol = np.chararray(self.world.get_size())
        for i in range(0,policy.max()+1):
            outPol[policy == i] = directionsTranslator[i]
            print(outPol)
        outPol[self.world.free_map()] = 'X'
        print(outPol)
        return outPol

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
