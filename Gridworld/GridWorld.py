import random

import gridworld_constants as gwc
import numpy as np


def get_random_policy():
    policy, value = random.choice(list(gwc.DIRECTIONS.items()))
    return policy


def policy_for_type(tile_type):
    if tile_type == gwc.TILE_TYPE_FREE:
        return get_random_policy()
    return tile_type


class GridWorld:

    def create_grids(self):
        value_grid = np.ndarray(shape=np.shape(self.source_grid), dtype=np.object)
        policy_grid = np.ndarray(shape=np.shape(self.source_grid), dtype=np.object)
        for i in range(np.shape(self.source_grid)[0]):
            for j in range(np.shape(self.source_grid)[1]):
                tile_type = self.source_grid[i][j]
                value_grid[(i, j)] = gwc.REWARDS[tile_type]
                policy_grid[(i, j)] = policy_for_type(tile_type)
        return value_grid, policy_grid

    def print_current_position(self, position):
        map = np.array(self.source_grid)
        map[position] = 'X'
        print(map)
        print(position)

    def step(self, position, action):
        action = gwc.DIRECTIONS[action]
        new_position = (position[0] + action[0], position[1] + action[1])
        if min(new_position) < 0 \
                or new_position[0] >= np.shape(self.source_grid)[0] \
                or new_position[1] >= np.shape(self.source_grid)[1]:
            new_position = position

        if self.source_grid[new_position] == gwc.TILE_TYPE_OBSTACLE:
            new_position = position

        return new_position

    def __init__(self, grid):
        self.source_grid = grid
        self.value_grid, self.policy_grid = self.create_grids()
