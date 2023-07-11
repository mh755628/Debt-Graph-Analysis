from genetic import *

from viz_graph import create_graph, Graph, Bipartite_Graph

g = Graph(['Alice', 'Bob', 'Clarie'], ['grey', 'grey', 'grey'])

g.add_edge(0, 1, 15)

# g.add_edge(1, 2, 5)

g.add_edge(0, 2, 15)

g.viz_graph()