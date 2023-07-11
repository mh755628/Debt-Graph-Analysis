import itertools

from viz_graph import create_graph

def solve(debt):
    p = [i for i in range(len(debt))]

    permute = list(itertools.permutations(p))

    mn = len(debt)

    #copy debt to ans

    ans = [x for x in debt]

    for perm in permute:
        nw_debt = []
        for i in perm:
            nw_debt.append(debt[i])
        
        in_debt, in_cred, edges = create_graph(nw_debt)
        

        if mn > len(edges):
            mn = len(edges)
            ans = [x for x in nw_debt]
    
    return ans, mn
    


    