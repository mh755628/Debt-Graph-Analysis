from random import shuffle, randint

POPULATION_SIZE = 25
MAXIMUM_WEIGHT = 20

n = randint(1, POPULATION_SIZE)
m = randint(1, n * (n - 1) // 2)

input_file_path = "input.txt"

edge = []
adj = [[0] * n for _ in range(n)]

for _ in range(m):
    a, b, c = randint(0, n - 1), randint(0, n - 1), randint(1, MAXIMUM_WEIGHT)
    if a == b:
        continue
    adj[a][b] += c

for i in range(n):
    for j in range(n):
        mn = min(adj[i][j], adj[j][i])
        adj[i][j] -= mn
        adj[j][i] -= mn

for i in range(n):
    for j in range(n):
        if adj[i][j] > 0:
            edge.append((i, j, adj[i][j]))

m = len(edge)




with open(input_file_path, "w") as f:
    #clear file
    f.write("")
    #write n, m
    f.write(str(n) + " " + str(m) + "\n")


    #write edges

    for a, b, c in edge:
        f.write(str(a) + " " + str(b) + " " + str(c) + "\n")


    

