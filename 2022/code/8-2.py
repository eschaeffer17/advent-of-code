Day = '8-1'

from common import read_daily_input
import numpy as np

aoc_input = read_daily_input(Day)
aoc_matrix = np.matrix([[int(i[j]) for j in range(len(i))] for i in aoc_input])

rows = aoc_matrix.shape[0]
columns = aoc_matrix.shape[1]

visible_trees = []

for i in range(1,rows-1):
    for j in range(1,columns-1):
        val = aoc_matrix[i,j]
        up = aoc_matrix[0:i,j].getA1()[::-1]
        left = aoc_matrix[i,0:j].getA1()[::-1]
        right = aoc_matrix[i,j+1:columns].getA1()
        down = aoc_matrix[i+1:rows,j].getA1()
        
        try:
            up_val = next(x for x, y in enumerate(up) if y >= val)+1
        except:
            up_val = len(up)
        try:
            left_val = next(x for x, y in enumerate(left) if y >= val)+1
        except:
            left_val = len(left)
        try:
            right_val = next(x for x, y in enumerate(right) if y >= val)+1
        except:
            right_val = len(right)
        try:
            down_val = next(x for x, y in enumerate(down) if y >= val)+1
        except:
            down_val = len(down)
        
        visible = (up_val * left_val * right_val * down_val)
        visible_trees.append(visible)

print(max(visible_trees))