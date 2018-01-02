
import numpy as np

class GridWorld:

    def __init__(self, path):
        self.map = readFile(path)
        
    def readFile(self, path):
        tmp = []
        with open('3by4.grid') as f:
            for line in f.readlines():
                tmp.append(line.split())
        return np.array(tmp)

    ###readfile
    ### get file name
    filename = '3by4.grid'
    file = open(filename, 'r')
    out2 = file.readlines()
    print(len(out2))



    print(np.shape(grid))
