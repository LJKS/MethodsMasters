import os

import numpy as np
from GridWorld import GridWorld
from MDP import MDP


def get_file_path():
    '''
    ask user to enter path to grid file
    :return: the path entered
    '''
    path = ''
    exists = False
    while not exists:
        path = input('Please enter the path to gridfile:')
        path = path.strip()
        exists = os.path.exists(path)
        if not exists:
            print('Please enter an existing path!')
    return path


def get_gamma():
    '''
    ask user for gamma value for policy evaluation
    :return: entered gamma value
    '''
    gamma = 2
    while gamma < 0 or gamma > 1:
        try:
            gamma = float(input('Please enter a gamma value between 0 and 1:'))
        except:
            print('Please enter a Float value between 0 and 1!')
    return gamma


def get_evaluation_steps():
    '''
    ask user for max policy evaluation steps
    :return: entered amount of steps
    '''
    steps = 0
    while steps <= 0:
        try:
            steps = int(input('Please specify the number of policy evaluation steps:'))
        except:
            print('Please enter an Integer value!')
    return steps

def get_move_cost():
    '''
    ask user for move costs fore each single move
    :return: entered amount of costs
    '''
    steps = 0
    move = False
    while not move:
        try:
            steps = float(input('Please enter the move cost to move from a free field (value from the lecture was -0.04):'))
            move = True
        except:
            print('Please enter an Float value!')
    return steps

def load_grid(url):
    '''
    loads the grid file and turns it into numpy array
    :param url: the path to load from
    :return: a numpy array based on grid
    '''
    with open(url) as file:
        lines = np.array([i.split() for i in file.readlines()])
    return lines

def start_again():
    start = False
    start_again = False
    while not start:
        user_input = input('Do you want to start again? (y/n)')
        #user_input = user_input.strip()
        if user_input == 'y':
            start_again = True
            start = True
        elif user_input == 'n':
            start_again = False
            start = True
        else:
            print('Please enter y or n!')
    return start_again

def start_grid_mdp():
    '''
    starts the program, restarts if the user wants to
    '''
    grid = load_grid(get_file_path())
    world = GridWorld(grid)
    move_costs = get_move_cost()
    gamma = get_gamma()
    eval_steps = get_evaluation_steps()
    MDP(world, eval_steps, gamma, move_costs)
    if start_again():
        start_grid_mdp()


if __name__ == '__main__':
    start_grid_mdp()
