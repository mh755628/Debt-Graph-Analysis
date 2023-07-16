n = 5
m = 12

# f.write(str(n) + " " + str(m) + "\n")

import random

edges = []

edges.append((0, 1, 20))
edges.append((0, 2, 20))
edges.append((4, 3, 20))

for i in range(m - 3):
    length = random.randint(2, n)

    perm = [i for i in range(n)]
    random.shuffle(perm)

    cycle = perm[:length]

    weight = random.randint(1, 10)

    for i in range(length):
        # print(cycle[i], cycle[(i + 1) % len], weight)
        edges.append((cycle[i], cycle[(i + 1) % length], weight))


matrix = [[0] * n for _ in range(n)]

for u, v, w in edges:
    matrix[u][v] += w

edges = []

for i in range(n):
    for j in range(n):
        mn = min(matrix[i][j], matrix[j][i])
        matrix[i][j] -= mn
        matrix[j][i] -= mn
        if matrix[i][j] > 0:
            edges.append((i, j, matrix[i][j]))


with open('input.txt', 'w') as f:

    f.write("") 

    mm = len(edges)

    f.write(str(n) + " " + str(mm) + "\n")

    for a, b, c in edges:
        f.write(str(a) + " " + str(b) + " " + str(c) + "\n")

    