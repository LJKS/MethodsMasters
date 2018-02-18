import random

import numpy as np
import pandas as pd

import QLearning.config as config


def print_matrix(matrix, text):
    """
    prints a given matrix in a certain format with the given text as headline
    """
    pd.options.display.float_format = '{:,.3f}'.format
    grid = pd.DataFrame(matrix)
    print('\n' + text + '\n', grid.to_string(index=True))


class Qlearn:

    def get_random_start(self):
        """
        chooses a random start state/field from all legal start states
        :return: start state
        """
        tile_type = config.TILE_TYPE_OBSTACLE
        coordinate = [0, 0]
        while tile_type != config.TILE_TYPE_FREE:
            coordinate = np.random.choice(self.gridworld.source_grid.shape[0], 2, replace=False)
            tile_type = self.gridworld.source_grid[coordinate[0], coordinate[1]]
        return coordinate

    def get_next_position(self, position, action):
        """
        Returns the destination state after doing an action at certain position
        - result depends on transition probabilities
        - 80% to do the actual action, 10% to do left/right action
        :param position: the current position / state
        :param action: the action to perform in the current state
        :return: the new position after doing action in position
        """
        intended_destination, side_step1, side_step2 = self.gridworld.side_step(position, action)
        probability = random.random()
        if probability <= config.PROBABILITIES[0]:
            return intended_destination
        else:
            return random.choice((side_step1, side_step2))

    def agent_terminated(self):
        """
        checks whether the agent has reached a terminal state (goal or pit)
        :return: if the agent has reached the goal or other terminal state
        """
        tile_type = self.gridworld.source_grid[self.current_agent_position[0], self.current_agent_position[1]]
        return tile_type == config.TILE_TYPE_PIT or tile_type == config.TILE_TYPE_END

    def on_episode_end(self):
        """
        assigns a new start state and saves the old policy to compare to for convergence
        """
        # assign agent new start state
        self.current_agent_position = self.get_random_start()
        # reset the value grid for current episode
        self.gridworld.reset_value_grid()
        # save the old policy to check whether it changes
        self.old_values = np.copy(self.target_values)
        self.episodes += 1
        print("running through grid... ", self.episodes)

    def policy_converged(self):
        """
        checks whether the policy converged and returns result
        """
        if np.array_equal(self.old_values, self.target_values) and self.episodes > 1:
            self.convergence_count -= 1
            if self.convergence_count <= 0:
                print('CONVERGED after ' + str(self.episodes - config.CONVERGENCE_COUNT) + ' episodes')
                return True
        else:
            self.convergence_count = config.CONVERGENCE_COUNT
        return False

    def calculate_q(self, position, new_position, action):
        """
        the q value function, calculates the new q-value for position/state
        :param position: the current state/position
        :param new_position:  the next state/position = prime state
        :param action: the action that should be taken from state
        :return: the updated q value
        """
        # v(s) <-- v(s) + alpha(r+gamma*v(s')-v(s))
        old_value = self.gridworld.action_value_grid[(position[0], position[1])][action]
        prime_value = self.target_values[(new_position[0], new_position[1])]
        q_value = old_value + self.learning_rate * (self.move_costs + self.discount * prime_value - old_value)
        return q_value

    def get_max_action_value(self, position):
        """
        returns the most greedy action possible from the state / position and its value
        :param position: the state from which the action should be taken
        :return: the most greedy action according to the action-value matrix and its corresponding value
        """
        max_value = None
        action = None
        for key, value in self.gridworld.action_value_grid[(position[0], position[1])].items():
            if max_value is None or value >= max_value:
                max_value = value
                action = key
        return action, max_value

    def choose_action(self, position):
        """
        chooses legal action according to epsilon soft policy
        :param position: the current state/position on which the action should be done
        :return: the action to follow
        """
        actions = list(config.DIRECTIONS.keys())
        # best action according to greedy policy
        action, value = self.get_max_action_value(position)
        # use epsilon soft policy to choose action
        probability = random.random()
        # remove best action from list of other actions
        actions.remove(action)
        # calculate new epsilon as it decreases over time
        epsilon = self.exploration_rate * pow(0.9, self.episodes)
        if probability > 1 - epsilon + (epsilon / len(config.DIRECTIONS)):
            action = random.choice(actions)
        return action

    def print_result(self):
        """ prints the value matrix and the policy matrix"""
        print_matrix(self.gridworld.policy_grid, '(Target) Policy:')
        print_matrix(self.target_values, '(Target) Policy Values:')
        print('\n')

    def step(self, print_values=False):
        """
        agent takes one step and calculates q value
        - chooses action to take according to epsilon soft policy
        - updates values in action-value grid
        - updates greedy policy
        """
        # check if not in terminal state, start new episode in case
        if self.agent_terminated():
            self.on_episode_end()

        position = self.current_agent_position
        # choose an action according to an epsilon soft policy
        action = self.choose_action(position)
        # do a step (possible outcome depending on transition probabilities)
        self.current_agent_position = self.get_next_position(position, action)
        # update values
        value = self.calculate_q(position, self.current_agent_position, action)
        self.gridworld.action_value_grid[(position[0], position[1])][action] = value
        self.gridworld.value_grid[(position[0], position[1])] = value
        # get greedy action and its value
        greedy_action, max_value = self.get_max_action_value(position)
        # update greedy policy and values
        self.gridworld.policy_grid[(position[0], position[1])] = greedy_action
        # round the max values to a certain precision
        self.target_values[(position[0], position[1])] = round(max_value, 3)
        print(str(action) + ' from ' + str(position) + " to " + str(self.current_agent_position))
        if print_values:
            print_matrix(self.gridworld.value_grid, '(Behaviour) Policy Values - current episode:')

    def single_step(self):
        """
        agent takes one step and updated matrix is displayed
        """
        self.step(print_values=True)

    def multi_steps(self, print_result=True):
        """
        all steps for one episode:
        iteration until agent ends up in end state/ goal state
        displays value and policy matrices when goal state reached
        """
        if self.agent_terminated():
            self.on_episode_end()
        while not self.agent_terminated():
            # step as long as needed
            self.step()
        if print_result:
            self.print_result()

    def step_till_convergence(self):
        """
        complete automatic q-learning which stops when the policy converges
        prints the resulting value matrix and policy
        """
        while not self.policy_converged():
            # step as long as needed
            self.multi_steps(print_result=False)
        self.print_result()

    def user_action(self):
        """
        asks the user which option to run:
        - a manual step wise q-value update
        - an automatic update of q values until the agent reaches a terminal state
        - an automatic update until the policy converges
        """
        while not self.policy_converged():
            user_input = input('Please choose what to do next:\n'
                               'Manual stepwise q-value update for one episode    (m)\n'
                               'Automatic q-value update for one episode          (a)\n'
                               'Automatic q-value update until convergence        (q)\n'
                               )
            if user_input == 'm':
                self.single_step()
            elif user_input == 'a':
                self.multi_steps()
            elif user_input == 'q':
                self.step_till_convergence()
            else:
                print('Please enter m or a or q!')

    def __init__(self, gridworld, move_costs, discount, learning_rate, exploration_rate):
        """
        Initalizes the q-learning program
        :param gridworld:  the grid to work with
        :param move_costs: the moving costs
        :param discount: the gamma value for the evaluation
        :param learning_rate: the learning rate/alpha value to use
        :param exploration_rate: the exploration rate for epsilon soft policy
        """
        self.gridworld = gridworld
        self.move_costs = move_costs
        self.discount = discount
        self.learning_rate = learning_rate
        self.exploration_rate = exploration_rate
        # sets a random legal start position for the agent
        self.current_agent_position = self.get_random_start()
        # number of episodes done
        self.episodes = 0
        # the values for the greedy/target policy
        self.target_values = np.copy(self.gridworld.value_grid)
        # the values to compare to for convergence
        self.old_values = None
        # the amount of episodes that need to run and not change to determine convergence
        self.convergence_count = config.CONVERGENCE_COUNT
        # ask for user input on possible options
        self.user_action()
