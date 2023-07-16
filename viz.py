from viz_graph import Graph, create_graph, Bipartite_Graph

def read(path = "input.txt"):
    with open(path, "r") as f:
        # n, m = map(int, input().split())
        n, m = map(int, f.readline().split())

        debt = [0] * n

        for _ in range(m):
            a, b, c = map(int, f.readline().split())
            debt[a] += c
            debt[b] -= c

        
        in_debt, in_cred, edges = create_graph(debt)

        B = Bipartite_Graph(in_debt, in_cred, ['red', 'blue'])

        for u, v, w in edges:
            B.add_edge(u, v, w)

        B.viz_graph()



def read1(path = "input.txt"):
    with open(path, "r") as f:
        # n, m = map(int, input().split())
        n, m = map(int, f.readline().split())

        g = Graph([i for i in range(n)], ['blue' for _ in range(n)])

        for _ in range(m):
            a, b, c = map(int, f.readline().split())
            g.add_edge(a, b, c)

        g.viz_graph()
        

read()

read1()