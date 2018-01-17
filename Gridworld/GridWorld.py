import random

import config
import numpy as np


def get_random_action():
    """
    static method, returns a random action from possible actions in gridworld_constants
    :return: a random action from gridworld_constants.DIRECTIONS
    """
    action, value = random.choice(list(config.DIRECTIONS.items()))
    return action


def action_for_tile_type(tile_type):
    """
    static method, returns a random possible action depending on tile type
    - only free tiles need an action for policy
    :param tile_type: the type
    :return: random action if free tile, otherwise the entered tile type
    """
    if tile_type == config.TILE_TYPE_FREE:
        return get_random_action()
    return tile_type


class GridWorld:

    def create_grids(self):
        """
        create needed grid representation based on source_grid
        value_grid = initial values for tile types
        policy_grid = random action assigned to each free tile
        :return: the value_grid and policy_grid
        """
        value_grid = np.ndarray(shape=np.shape(self.source_grid), dtype=np.object)
        policy_grid = np.ndarray(shape=np.shape(self.source_grid), dtype=np.object)
        for i in range(np.shape(self.source_grid)[0]):
            for j in range(np.shape(self.source_grid)[1]):
                tile_type = self.source_grid[i][j]
                value_grid[(i, j)] = config.REWARDS[tile_type]
                policy_grid[(i, j)] = action_for_tile_type(tile_type)
        return value_grid, policy_grid

    def step(self, position, action):
        """
        calculates where one ends up after doing given action in certain position
        :param position: the start position in the grid , tuple (x,y)
        :param action: the action to perform (based on actions in config.DIRECTIONS
        :return: the new position after step was done, tuple (x,y)
        """
        action = config.DIRECTIONS[action]
        new_position = (position[0] + action[0], position[1] + action[1])
        if min(new_position) < 0 \
                or new_position[0] >= np.shape(self.source_grid)[0] \
                or new_position[1] >= np.shape(self.source_grid)[1]:
            new_position = position

        if self.source_grid[new_position] == config.TILE_TYPE_OBSTACLE:
            new_position = position

        return new_position

    def reset_value_grid(self):
        """
        resets the value grid to initial values
        """
        value_grid = np.ndarray(shape=np.shape(self.source_grid), dtype=np.object)
        for i in range(np.shape(self.source_grid)[0]):
            for j in range(np.shape(self.source_grid)[1]):
                value_grid[(i, j)] = config.REWARDS[self.source_grid[i][j]]
        self.value_grid = value_grid

    def __init__(self, grid):
        """
        a grid object holding different infos
        - source grid = the original numpy matrix
        - value grid = grid based on source holding current grid tile values
        - policy grid = grid based on source holding certain action for each grid tile
        :param grid: the numpy matrix as source layout
        """
        self.source_grid = grid
        self.value_grid, self.policy_grid = self.create_grids()
