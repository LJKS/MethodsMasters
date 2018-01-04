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
    return path


def get_gamma():
    '''
    ask user for gamma value for policy evaluation
    :return: entered gamma value
    '''
    gamma = 2
    while gamma < 0 or gamma > 1:
        gamma = float(input('Please enter a gamma value between 0-1:'))
    return gamma


def get_evaluation_steps():
    '''
    ask user for max policy evaluation steps
    :return: entered amount of steps
    '''
    steps = 0
    while steps <= 0:
        steps = int(input('Please specify the number of policy evaluation steps:'))
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


def start_grid_mdp():
    '''
    starts the program, restarts after finish
    :return:
    '''
    grid = load_grid(get_file_path())
    world = GridWorld(grid)
    gamma = get_gamma()
    eval_steps = get_evaluation_steps()
    MDP(world, eval_steps, gamma)
    start_grid_mdp()


if __name__ == '__main__':
    start_grid_mdp()
