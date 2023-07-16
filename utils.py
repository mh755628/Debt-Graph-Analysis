def input_handler():

    n, m = map(int, input().split())

    debt = [0] * n
    for _ in range(m):
        a, b, c = map(int, input().split())
        debt[a] += c
        debt[b] -= c
    
    nw_debt = []

    for x in debt:
        if x != 0:
            nw_debt.append(x)
    
    return nw_debt