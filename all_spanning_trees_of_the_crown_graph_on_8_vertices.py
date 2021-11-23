"""
This code is made for generation of all spanning trees of the crown graph on 8 vertices.
"""

import itertools

import networkx as nx
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("Agg")

graph = nx.Graph()

graph.add_node('A')
graph.add_node('B')
graph.add_node('C')
graph.add_node('D')
graph.add_node('A′')
graph.add_node('B′')
graph.add_node('C′')
graph.add_node('D′')

graph.add_edge('A', 'B′')
graph.add_edge('A', 'C′')
graph.add_edge('A', 'D′')
graph.add_edge('B', 'A′')
graph.add_edge('B', 'C′')
graph.add_edge('B', 'D′')
graph.add_edge('C', 'A′')
graph.add_edge('C', 'B′')
graph.add_edge('C', 'D′')
graph.add_edge('D', 'A′')
graph.add_edge('D', 'B′')
graph.add_edge('D', 'C′')


variants = list(itertools.combinations(graph.edges(), 7))


pos = {
    'A': (-1.5, 0.5),
    'A′': (-1.5, -0.5),
    'B': (-0.5, 0.5),
    'B′': (-0.5, -0.5),
    'C': (0.5, 0.5),
    'C′': (0.5, -0.5),
    'D': (1.5, 0.5),
    'D′': (1.5, -0.5)}

index = 1

Unique_Trees=list()

for combination in variants:
    G=nx.Graph()

    G.add_nodes_from(graph)
    G.add_edges_from(combination)

    connected=(nx.number_connected_components(G)==1)

    if connected:
        nx.draw_networkx(G,
                         pos=pos,
                         node_color='red',
                         edge_color='black',
                         font_size=20,
                         node_size=1000)
        filename=str(index)+'.png'
        plt.savefig(filename)
        plt.close('all')
        index+=1