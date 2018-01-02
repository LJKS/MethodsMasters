
import numpy as np

class GridWorld:

    def __init__(self, path):
        self.directions = {'up':[-1,0], 'down':[1,0], 'left': [0,-1], 'right':[0,1]}
        self.values = {'F': -0.04, 'O': 0, 'P': -1, 'E': 1}
        self.map = self.read_file(path)
        self.build_weightmap()

    def read_file(self, path):
        tmp = []
        with open(path) as f:
            for line in f.readlines():
                tmp.append(line.split())
        return np.array(tmp)

    def build_weightmap(self):
        weight_map = np.zeros(np.shape(self.map))
        for key in self.values:
            key_map = self.map == key
            key_map = key_map.astype(int)*self.values[key]
            weight_map += key_map
        print(weight_map)
        return weight_map

    def step(self, state, action):
        goal = state + self.directions[action]
        relative_pos = self.map.shape - goal
        #special treatment for endstate
        if self.map[state] == 'P' or map[state] == 'E':
            return 'END'
        #check left and upper out of bounds
        elif goal.min()<0:
            return state
        #check lower and right out of bounds
        elif relative_pos.min() < 0:
            return state
        #check for run against wall
        elif self.map[goal] == 'O':
            return state
        #else we just take the step
        else:
            return goal

    def get_weightmap(self):
        return self.weight_map

    def get_size(self):
        return np.shape(self.map)
