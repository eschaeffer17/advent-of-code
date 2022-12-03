Day = '2-2'

from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read().splitlines()

possible_hands = ['A','B','C']
possible_combinations = []

for i in possible_hands:
    for j in possible_hands:
        if i==j:
            outcome = 'Y'
            point_val = 3
        elif (i=='B' and j=='A')|(i=='C' and j=='B')|(i=='A' and j=='C'):
            outcome = 'Z'
            point_val = 6
        else:
            outcome = 'X'
            point_val = 0
        possible_combinations.append([i,j,outcome,point_val])

G = nx.DiGraph()

#G.add_nodes_from(['A','B','C'])
G.add_node('A',score=1)
G.add_node('B',score=2)
G.add_node('C',score=3)

for i in possible_combinations:
    G.add_edge(i[0],i[1],result=i[2],score=i[3])

scores = []

for i in aoc_input:
    j = i.split(' ')
    scores.append(*(d['score']+G.nodes[u]['score'] for u,v,d in G.edges(data=True) if d['result']==j[1] and v==j[0]))

answer = sum(scores)

# pos=nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, font_weight='bold')
# edge_weight = nx.get_edge_attributes(G,'score')
# nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
# plt.show()
