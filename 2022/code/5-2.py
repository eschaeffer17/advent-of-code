Day = '5-2'

from common import read_daily_input

aoc_input = read_daily_input(Day,'\n\n')


puzzle_conf = [i.split('\n') for i in aoc_input]
puzzle_conf[1].remove('')

num_stacks = 9
stack_conf = []
for i in range(num_stacks):
    stack_conf.append([])

for i in puzzle_conf[0]:
    layout = i[1:35:4]
    for j in range(len(layout)):
        if layout[j]!=' ':
            stack_conf[j].append(layout[j])

stack_dict = {}
for i in stack_conf:
    stack_dict[i[-1]]=i[0:-1]

for i in puzzle_conf[1]:
    step = i.split(' ')[1:6:2]
    crate = stack_dict[step[1]][0:int(step[0])]
    del stack_dict[step[1]][0:int(step[0])]
    stack_dict[step[2]] = crate + stack_dict[step[2]]

print(''.join([stack_dict[i][0] for i in stack_dict.keys()]))