import os

import numpy as np
from GridWorld import GridWorld
from MDP import MDP


def get_file_path():
    path = ''
    while not os.path.exists(path):
        path = input('Please enter the path to gridfile:')
    return path


def get_gamma():
    gamma = 2
    while gamma < 0 or gamma > 1:
        gamma = float(input('Please enter a gamma value between 0-1:'))
    return gamma


def get_evaluation_steps():
    steps = 0
    while steps <= 0:
        steps = int(input('Please specify the number of policy evaluation steps:'))
    return steps


def load_grid(url):
    with open(url) as file:
        lines = np.array([i.split() for i in file.readlines()])
    return lines


if __name__ == '__main__':
    grid = load_grid(get_file_path())
    world = GridWorld(grid)
    gamma = get_gamma()
    eval_steps = get_evaluation_steps()
    mdp = MDP(world, eval_steps, gamma)
