Day = '2-1'

from pathlib import Path
import networkx as nx
import matplotlib.pyplot as plt

input_path = "../inputs/"+Day+".txt"
path = Path(__file__).parent / input_path

with path.open() as f:
    aoc_input = f.read().splitlines()

G = nx.DiGraph()

G.add_nodes_from(['A','B','C'])
G.add_node('X',score=1)
G.add_node('Y',score=2)
G.add_node('Z',score=3)
G.add_weighted_edges_from([('X','A',3),('Y','A',6),('Z','A',0),('X','B',0),('Y','B',3),('Z','B',6),('X','C',6),('Y','C',0),('Z','C',3)])

print(G.nodes['X']['score'])

print(G.nodes())
print(G.edges())

game = ['A Y','B Y']
scores = []

for i in aoc_input:
    j = i.split(' ')
    scores.append(G.edges[(j[1],j[0])]['weight']+G.nodes[j[1]]['score'])

answer = sum(scores)

# pos=nx.spring_layout(G)
# nx.draw(G, pos, with_labels=True, font_weight='bold')
# edge_weight = nx.get_edge_attributes(G,'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels = edge_weight)
# plt.show()

#print([x.split(' ') for x in aoc_input])