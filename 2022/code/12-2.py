Day = '12-1'

from common import read_daily_input
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import math

aoc_input = read_daily_input(Day)

G = nx.DiGraph()

aoc_matrix = np.matrix([[i[j] for j in range(len(i))] for i in aoc_input])
rows = aoc_matrix.shape[0]
columns = aoc_matrix.shape[1]

for i in range(rows):
    for j in range(columns):
        if aoc_matrix[i,j]=='S':
            val = 'a'
            pos = 'Starting'
        elif aoc_matrix[i,j]=='E':
            val = 'z'
            pos = 'Ending'
        else:
            val = aoc_matrix[i,j]
            pos = None
        G.add_node(str(i)+':'+str(j), height=ord(val)-96, position=pos)

for i in range(rows):
    for j in range(columns):
        neighbors = [str(i-1)+':'+str(j), str(i+1)+':'+str(j), str(i)+':'+str(j-1), str(i)+':'+str(j+1)]
        neighbors = [x for x in neighbors if int(x.split(':')[0]) in range(rows) and int(x.split(':')[1]) in range(columns)]
        for y in neighbors:
            if G.nodes[y]['height']<=G.nodes[str(i)+':'+str(j)]['height']+1:
                G.add_edge(str(i)+':'+str(j),y)

possible_starts = [x for x in G.nodes if G.nodes[x]['height']==1]
end = [x for x in G.nodes if G.nodes[x]['position']=='Ending'][0]
outcomes = []
for start in possible_starts:
    try:
        path_length = len(nx.shortest_path(G, start, end))-1
        outcomes.append(path_length)
    except:
        path_length = None

print(min(outcomes))