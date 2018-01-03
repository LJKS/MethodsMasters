import numpy as np

import gridworld_constants as gwc


class MDP:

    def calculate_action(self, position):
        action = self.gridworld.policy_grid[position]
        if (action in gwc.DIRECTIONS):
            # TODO find a better way to add the other directions
            forward_step = self.gridworld.step(position, action)
            if action == gwc.DIRECTION_NORTH or action == gwc.DIRECTION_SOUTH:
                side_step1 = self.gridworld.step(position, gwc.DIRECTION_EAST)
                side_step2 = self.gridworld.step(position, gwc.DIRECTION_WEST)
            elif action == gwc.DIRECTION_WEST or action == gwc.DIRECTION_EAST:
                side_step1 = self.gridworld.step(position, gwc.DIRECTION_NORTH)
                side_step2 = self.gridworld.step(position, gwc.DIRECTION_SOUTH)

            cost = gwc.REWARDS[gwc.TILE_TYPE_FREE]
            forward_cost = gwc.PROBABILITIES[0] * self.gridworld.value_grid[forward_step]
            side_step1_cost = gwc.PROBABILITIES[1] * self.gridworld.value_grid[side_step1]
            side_step2_cost = gwc.PROBABILITIES[2] * self.gridworld.value_grid[side_step2]
            reward = cost + self.gamma * (forward_cost + side_step1_cost + side_step2_cost)
            return reward

        return self.gridworld.value_grid[position]

    def evaluate_policy(self):
        evaluated_grid = np.array(self.gridworld.value_grid)
        n = 0
        while n <= self.evaluation_steps:
            for x in range(np.shape(self.gridworld.policy_grid)[0]):
                for y in range(np.shape(self.gridworld.policy_grid)[1]):
                    evaluated_grid[(x, y)] = self.calculate_action((x, y))
            n += 1
            self.gridworld.value_grid = evaluated_grid

    def iterate_policy(self):
        greedy_policy = np.array(self.gridworld.policy_grid)
        # TODO: policy iteration

        self.gridworld.policy_grid = greedy_policy

    def __init__(self, gridworld, evaluation_steps, gamma):
        self.gridworld = gridworld
        self.evaluation_steps = evaluation_steps
        self.gamma = gamma
        self.evaluate_policy()
        self.iterate_policy()
        print('\n Loaded Grid:')
        print(self.gridworld.source_grid)
        print('\n Optimal Policy:')
        print(self.gridworld.policy_grid)
        print('\n Policy values:')
        print(self.gridworld.value_grid)
