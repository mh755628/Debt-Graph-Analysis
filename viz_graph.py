import networkx as nx
import matplotlib.pyplot as plt

def create_graph(tmp):
    debt = [x for x in tmp]
    in_debt = []
    in_cred = []

    for i in range(0, len(debt)):
        if debt[i] > 0:
            in_debt.append(i)
        else:
            in_cred.append(i)
            debt[i] = -debt[i]

    edges = []

    i = 0
    for p in in_debt:
        while debt[p] > 0:
            j = 0
            for q in in_cred:
                if debt[q] > 0:
                    mn = min(debt[p], debt[q])
                    if mn > 0:
                        edges.append((i, j, mn))
                    debt[p] -= mn
                    debt[q] -= mn
                j += 1
        i += 1

    return in_debt, in_cred, edges   

     

class Graph:
    def __init__(self, nodes, colors=None):
        self.nodes = nodes
        self.edges = [[] for _ in range(len(nodes))]
        self.colors = colors

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))

    #vissualize graph
    def viz_graph(self):

        #increase size of nodes

        G = nx.DiGraph()


        for i in range(len(self.nodes)):
            G.add_node(self.nodes[i])

        edge_labels = {}
        width = []
        for i in range(len(self.nodes)):
            for j in range(len(self.edges[i])):
                G.add_edge(self.nodes[i], self.nodes[self.edges[i][j][0]])
                edge_labels[(self.nodes[i], self.nodes[self.edges[i][j][0]])] = self.edges[i][j][1]
                width.append(self.edges[i][j][1])


        node_sizes = [1200 for _ in range(len(self.nodes))]
        colors = ['blue' for _ in range(len(self.nodes))]

        plt.rcParams['toolbar'] = 'None'

        #normalize width

        max_width = max(width)

        for i in range(len(width)):
            width[i] = width[i] / max_width * 5


        pos = nx.circular_layout(G)
        nx.draw_networkx_nodes(G, pos, node_size=node_sizes, node_color=self.colors)
        nx.draw_networkx_labels(G, pos)
        nx.draw_networkx_edges(G, pos, arrows=True, width=width, arrowstyle='->', arrowsize=40)
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.axis('off')

        # random = np.random.randint(1000000)

        #save fig
        plt.savefig('normal.png', bbox_inches='tight', pad_inches=0, dpi=100)
        # plt.show()

        #save fig
        plt.savefig('graph.png', bbox_inches='tight', pad_inches=0, dpi=100)

        #remove menu bar
        

        #waitkey q
        plt.waitforbuttonpress(0)
        plt.close()


class Bipartite_Graph:
    def __init__(self, nodeset1, nodeset2, colors=None):
        self.nodeset1 = nodeset1
        self.nodeset2 = nodeset2
        self.edges = [[] for _ in range(len(nodeset1))]
        self.colors = colors

    def add_edge(self, u, v, w):
        self.edges[u].append((v, w))

    #vissualize graph
    def viz_graph(self):
        B = nx.Graph()
        plt.rcParams['toolbar'] = 'None'


        for i in range(len(self.nodeset1)):
            B.add_node(self.nodeset1[i])
        for i in range(len(self.nodeset2)):
            B.add_node(self.nodeset2[i])

        
        edge_labels = {}
        width = []

        for i in range(len(self.nodeset1)):
            for j in range(len(self.edges[i])):
                B.add_edge(self.nodeset1[i], self.nodeset2[self.edges[i][j][0]])
                edge_labels[(self.nodeset1[i], self.nodeset2[self.edges[i][j][0]])] = self.edges[i][j][1]
                width.append(self.edges[i][j][1])

        # node_sizes = [1200 for _ in range(len(self.nodeset1) + len(self.nodeset2))]

        node_size1 = [1200 for _ in range(len(self.nodeset1))]
        node_size2 = [1200 for _ in range(len(self.nodeset2))]

        #normalize width

        max_width = max(width)

        for i in range(len(width)):
            width[i] = width[i] / max_width * 8

        pos = nx.bipartite_layout(B, self.nodeset1)

        nx.draw_networkx_nodes(B, pos, nodelist=self.nodeset1, node_size=node_size1, node_color=self.colors[0])
        nx.draw_networkx_nodes(B, pos, nodelist=self.nodeset2, node_size=node_size2, node_color=self.colors[1])
        nx.draw_networkx_labels(B, pos)
        nx.draw_networkx_edges(B, pos, arrows=True, width=width, arrowstyle='->', arrowsize=40)
        nx.draw_networkx_edge_labels(B, pos, edge_labels=edge_labels)

        plt.axis('off')

        #save fig

        plt.savefig('bipartite.png', bbox_inches='tight', pad_inches=0, dpi=100)

        # plt.show()
        #waitkey q
        plt.waitforbuttonpress(0)
        plt.close()



# g = Graph(["Bob", "Alice", "Clarie"], ['blue', 'green', 'green'])



# g.add_edge(1, 0, 20)

# g.add_edge(1, 2, 5)

# g.add_edge(0, 2, 10)

# g.viz_graph()

# g = Bipartite_Graph(["Bob", "Alice", "Clarie"], ["a", "b", "c"], ['blue', 'green'])

# g.add_edge(1, 0, 20)

# g.add_edge(1, 2, 5)

# g.add_edge(0, 2, 10)

# g.viz_graph()   