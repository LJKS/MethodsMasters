import numpy as np
from gridWorld import GridWorld

class mdp:
    def __init__ (self, path):
        self.world = gridWorld.GridWorld(path)

hallo = mdp('3by4.grid')
