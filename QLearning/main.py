import os

import numpy as np

from QLearning.GridWorld import GridWorld
from QLearning.MDP import MDP
from QLearning.Qlearn import Qlearn


def get_file_path():
    """
    ask user to enter path to grid file
    :return: the path entered
    """
    path = ''
    exists = False
    while not exists:
        path = input('Please enter the path to gridfile:')
        path = path.strip()
        exists = os.path.exists(path)
        if not exists:
            print('Please enter an existing path!')
    return path


def get_zero_one_value(text):
    """
    helper function to ask user for a Float value between 0 and 1
    :param text: the text to display to user
    :return: the entered value
    """
    value = 2
    while value < 0 or value > 1:
        try:
            value = float(input(text))
        except ValueError:
            print('Please enter a Float value between 0 and 1!')
    return value


def get_discount():
    """
    ask user for gamma value for policy evaluation
    :return: entered gamma value
    """
    return get_zero_one_value('Please enter a discount value (gamma) between 0 and 1:')


def get_evaluation_steps():
    """
    ask user for max policy evaluation steps
    :return: entered amount of steps
    """
    steps = 0
    while steps <= 0:
        try:
            steps = int(input('Please specify the number of policy evaluation steps:'))
        except ValueError:
            print('Please enter a positive Integer value!')
    return steps


def get_move_cost():
    """
    ask user for move costs fore each single move / also called move reward
    :return: entered amount of costs
    """
    value = 0
    entered = False
    while not entered:
        try:
            value = float(input('Please enter the costs to move from a free field (value from the lecture was -0.04):'))
            entered = True
        except ValueError:
            print('Please enter a FLOAT value!')

    return value


def get_exploration_rate():
    """
    asks user for the exploration rate (epsilon value) for epsilon soft policy in q learning
    :return: entered epsilon value
    """
    return get_zero_one_value('Please enter an exploration rate (epsilon) for the epsilon-soft policy between 0-1:')


def get_learning_rate():
    """
    asks user for alpha, the learning rate
    :return: alpha according to user
    """
    return get_zero_one_value('Please enter a learning rate (alpha value) between 0-1:')


def load_grid(url):
    """
    loads the grid file and turns it into numpy array
    :param url: the path to load from
    :return: a numpy array based on grid
    """
    with open(url) as file:
        lines = np.array([i.split() for i in file.readlines()])
    return lines


def choose_mode():
    """
    asks user which program to start: MDP or Q-learning
    and starts chosen program
    """
    chosen = False
    while not chosen:
        user_input = input('Please choose a program: MDP (m) or Q-learning (q): (m/q) ')
        chosen = True
        if user_input == 'm':
            start_grid_mdp()
        elif user_input == 'q':
            start_q_learning()
        else:
            print('Please enter m or q!')
            chosen = False


def start_again():
    """
    asks the user whether to terminate the program or restart
    :return: boolean whether to restart
    """
    while True:
        user_input = input('Do you want to start again? (y/n)')
        if user_input == 'y':
            return True
        elif user_input == 'n':
            return False
        else:
            print('Please enter y or n!')


def setup_world():
    """
    load the grid and setup the gridworld
    :return: the gridworld based on loaded grid
    """
    world = GridWorld(load_grid(get_file_path()))
    return world


def start_grid_mdp():
    """
    starts the MDP program and collects all parameters
    """
    world = setup_world()
    move_costs = get_move_cost()
    gamma = get_discount()
    eval_steps = get_evaluation_steps()
    MDP(world, eval_steps, gamma, move_costs)


def start_q_learning():
    """
    starts the Q-learning program,  collects all  parameters
    """
    world = setup_world()
    move_costs = get_move_cost()
    gamma = get_discount()
    alpha = get_learning_rate()
    epsilon = get_exploration_rate()
    Qlearn(world, move_costs, gamma, alpha, epsilon)


def start():
    """
    starts the program and asks for a restart after chosen mode finishes
    """
    choose_mode()
    if start_again():
        start()


# TODO: remove me
def develop_start():
    world = GridWorld(load_grid('grids/3by4.grid'))
    move_costs = -0.04
    gamma = 1
    alpha = 0.5
    epsilon = 0.5
    Qlearn(world, move_costs, gamma, alpha, epsilon)
    if start_again():
        develop_start()


if __name__ == '__main__':
    # start()
    # TODO: remove me
    develop_start()
