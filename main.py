import numpy as np
with open('3by4.grid') as f:
    lines =np.array ([i.split() for i in f.readlines()])

print(lines)
# print(grid)
