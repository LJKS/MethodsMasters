
import numpy as np

def cleanLine(line):
    #...
    return line

###readfile
### get file name
filename = '3by4.grid'
file = open(filename, 'r')
out2 = file.readlines()
print(len(out2))

grid = np.zeros([1,1])
for line in out2:
    np.append(grid,cleanLine(np.array(line)),1)
out = np.array(list(out2))
print(type(out))
print(out.size)
print(out)
