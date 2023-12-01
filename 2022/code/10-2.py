Day = '10-2'

from common import read_daily_input
import numpy as np

aoc_input = read_daily_input(Day)

def action(step):
    if step.split(' ')[0]=='addx':
        num_cycles=2
        val=int(step.split(' ')[1])
    else:
        num_cycles=1
        val=0
    return num_cycles, val

def iterate_steps(aoc_input,starting_val):
    i = 0
    pos = 0
    lst = []
    while i<len(aoc_input):
        num_cycles, val = action(aoc_input[i])
        for j in range(num_cycles):
            if starting_val-1<=pos<=starting_val+1:
                output = '#'
            else:
                output = '.'
            if pos==39:
                pos=0
            else:
                pos+=1
            lst.append(output)
        starting_val+=val
        i+=1
    
    return lst

answer = iterate_steps(aoc_input,1)

for x in [''.join(answer[i*40:(i*40)+40]) for i in range(6)]:
    print(x)