from viz_graph import create_graph, Graph, Bipartite_Graph

from bruteforce import solve

from genetic import *

from tqdm import tqdm

#input

n, m = map(int, input().split()) # n: number of people m: number of relations
debt = [0] * n # debt[i]: debt of i-th person

for _ in range(m):
    a, b, c = map(int, input().split()) # a, b: people c: relation
    debt[a] += c
    debt[b] -= c

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

for i in tqdm(range(1000)):
    population = getNextGen(population, debt)

    if population[0].fitness < score:
        print("Generation", i, "score", population[0].fitness)
        # score = population[0].fitness(debt)
    
population.sort(key=lambda gene: gene.fitness)


nw_debt = [debt[i] for i in population[0].permutation]

print(debt, nw_debt)

in_debt, in_cred, edges = create_graph(nw_debt)



B = Bipartite_Graph(in_debt, in_cred, ['red', 'blue'])

for u, v, w in edges:
    # print(u, v, w)
    B.add_edge(u, v, w)

B.viz_graph()