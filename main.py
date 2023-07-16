from viz_graph import create_graph, Graph, Bipartite_Graph

from bruteforce import solve

from genetic import *

from tqdm import tqdm

#input

n, m = map(int, input().split()) # n: number of people m: number of relations
debt = [0] * n # debt[i]: debt of i-th person


# g1 = Graph([i for i in range(n)], ['grey' for i in range(n)])

for _ in range(m):
    a, b, c = map(int, input().split()) # a, b: people c: relation
    # g1.add_edge(a, b, c)
    debt[a] += c
    debt[b] -= c

# g1.viz_graph()

# exit()

tmp = []

for x in debt:
    if x != 0:
        tmp.append(x)



debt = tmp

print(debt)

n = len(debt)


population = getInitialPopulation(n, debt)


score = n * 10

# print("Bruteforce:")

# ans, mn = solve(debt)

# print("Score:", mn)

x = []
y = []

import matplotlib.pyplot as plt

for i in tqdm(range(10000)):
    population = getNextGen(population, debt)

    if population[0].fitness < score:
        print("Generation", i, "score", population[0].fitness)
        x.append(i)
        y.append(population[0].fitness)
        score = population[0].fitness
    
population.sort(key=lambda gene: gene.fitness)


nw_debt = [debt[i] for i in population[0].permutation]


in_debt, in_cred, edges = create_graph(nw_debt)


print(len(debt), score)


B = Bipartite_Graph(in_debt, in_cred, ['red', 'blue'])



for u, v, w in edges:
    # print(u, v, w)
    B.add_edge(u, v, w)

B.viz_graph()