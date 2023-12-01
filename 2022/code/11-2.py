Day = '11-1'

from common import read_daily_input
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

aoc_input = read_daily_input(Day,'\n\n')

G = nx.DiGraph()

for i in aoc_input:
    monkey_config = i.split('\n')
    monkey_num = monkey_config[0][7]
    starting_items = monkey_config[1].split(': ')[1].split(', ')
    operation = monkey_config[2].split('= ')[1]
    test = ' % ' + monkey_config[3].split('by ')[1] + ' == 0'

    G.add_node(monkey_num, items=starting_items, operation=operation, test=test, items_inspected=0)

for j in aoc_input:
    monkey_config = j.split('\n')
    monkey_num = monkey_config[0][7]
    true_result = monkey_config[4].split('monkey ')[1]
    false_result = monkey_config[5].split('monkey ')[1]

    G.add_edge(monkey_num,true_result,test_eval=True)
    G.add_edge(monkey_num,false_result,test_eval=False)

supermod = math.prod([int(G.nodes[x]['test'].split('=')[0].split('%')[1]) for x in G.nodes])

def play_round():
    for i in G.nodes:
        op = G.nodes[i]['operation']
        test_eq = G.nodes[i]['test']
        n = len(G.nodes[i]['items'])
        while 0 < n:
            G.nodes[i]['items_inspected']+=1
            result = eval(op.replace('old',G.nodes[i]['items'][0]))
            action = eval(str(result)+test_eq)
            throw_to_monkey = [i[0] for i in G[i].items() if i[1]['test_eval']==action][0]
            del G.nodes[i]['items'][0]
            G.nodes[throw_to_monkey]['items'].append(str(result % supermod))
            n = n - 1

def play_rounds(num_rounds):
    for round in range(num_rounds):
        play_round()

play_rounds(10000)

lst = [G.nodes[x]['items_inspected'] for x in G.nodes]
lst.sort()
print(lst[-1]*lst[-2])