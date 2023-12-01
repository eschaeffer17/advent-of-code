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
        up = aoc_matrix[0:i,j]
        left = aoc_matrix[i,0:j]
        right = aoc_matrix[i,j+1:columns]
        down = aoc_matrix[i+1:rows,j]

        visible = any([val>up.max(),val>left.max(),val>right.max(),val>down.max()])
        visible_trees.append(visible)

print(visible_trees.count(True) + (columns*2) + (rows*2) - 4)