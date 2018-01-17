import config
import numpy as np
import pandas as pd


class MDP:

    def calculate_action(self, position, action):
        """
         calculates the cost/reward for certain action on certain position
        :param position: the current position on the grid
        :param action: the action to be performed
        :return: reward/cost for doing currently assigned action on current position
        """

        if action in config.DIRECTIONS:
            # TODO find a better way to add the other directions
            forward_step = self.gridworld.step(position, action)
            if action == config.DIRECTION_NORTH or action == config.DIRECTION_SOUTH:
                side_step1 = self.gridworld.step(position, config.DIRECTION_EAST)
                side_step2 = self.gridworld.step(position, config.DIRECTION_WEST)
            elif action == config.DIRECTION_WEST or action == config.DIRECTION_EAST:
                side_step1 = self.gridworld.step(position, config.DIRECTION_NORTH)
                side_step2 = self.gridworld.step(position, config.DIRECTION_SOUTH)

            forward_cost = config.PROBABILITIES[0] * self.gridworld.value_grid[forward_step]
            side_step1_cost = config.PROBABILITIES[1] * self.gridworld.value_grid[side_step1]
            side_step2_cost = config.PROBABILITIES[1] * self.gridworld.value_grid[side_step2]
            reward = self.move_cost + self.gamma * (forward_cost + side_step1_cost + side_step2_cost)
            return reward

        return self.gridworld.value_grid[position]

    def choose_greedy_action(self, position):
        """
        helper function for policy improvement
        :returns most greedy action for a certain position in the grid
        """
        action = self.gridworld.policy_grid[position]
        if action in config.DIRECTIONS:
            max_value = self.calculate_action(position, action)
            for direction in config.DIRECTIONS:
                value = self.calculate_action(position, direction)
                if value > max_value:
                    max_value = value
                    action = direction
        return action

    def evaluate_policy(self):
        """
        evaluates current policy n-times
        - n defined by evaluation steps parameter of MDP
        - sets new value grid for Gridworld
        """
        self.gridworld.reset_value_grid()
        evaluated_grid = np.array(self.gridworld.value_grid)
        n = 0
        while n < self.evaluation_steps:
            for x in range(np.shape(self.gridworld.policy_grid)[0]):
                for y in range(np.shape(self.gridworld.policy_grid)[1]):
                    action = self.gridworld.policy_grid[(x, y)]
                    evaluated_grid[(x, y)] = self.calculate_action((x, y), action)
            n += 1
            self.gridworld.value_grid = evaluated_grid

    def improve_policy(self):
        """
        find a greedy policy
        - assigns a  new improved policy to Gridworld
        """
        greedy_policy = np.array(self.gridworld.policy_grid)
        for x in range(np.shape(self.gridworld.policy_grid)[0]):
            for y in range(np.shape(self.gridworld.policy_grid)[1]):
                greedy_policy[(x, y)] = self.choose_greedy_action((x, y))
        self.gridworld.policy_grid = greedy_policy

    def iterate_policy(self):
        """
        policy iteration until convergence
        - evaluate policy
        - improve policy
        """
        converged = False
        while not converged:
            old_policy = np.array(self.gridworld.policy_grid)
            self.evaluate_policy()
            self.improve_policy()
            converged = np.array_equal(old_policy, self.gridworld.policy_grid)
            self.calculation_string += '.'
            print(self.calculation_string)

    def print_output(self):
        """
        prints the data from the MDP:
        - the original grid handed it
        - the optimal policy found for the grid
        - the policy values of the optimal policy
        """
        grid = pd.DataFrame(self.gridworld.source_grid)
        print('\n Loaded Grid: \n', grid.to_string(index=False))
        policy = pd.DataFrame(self.gridworld.policy_grid)
        print('\n Optimal Policy: \n', policy.to_string(index=False))
        values = pd.DataFrame(self.gridworld.value_grid)
        print('\n Policy values: \n', values.to_string(index=False), '\n')

    def __init__(self, gridworld, evaluation_steps, gamma, move_cost):
        """
        Performs a policy iteration for a given gridworld and prints the outcome

        :param gridworld: The gridworld to work with
        :param evaluation_steps: the maximum amount of policy evaluation steps to be performed
        :param gamma: the gamma value for the evaluation (future reward)
        """
        # calculation string printed as user feedback
        self.calculation_string = 'Calculating '
        self.gridworld = gridworld
        self.evaluation_steps = evaluation_steps
        self.gamma = gamma
        self.move_cost = move_cost
        self.iterate_policy()
        self.print_output()
