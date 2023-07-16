from utils import *

def main(debt = None):
    if debt is None:
        debt = input_handler()
    n = len(debt)

    # print(debt)

    dp = [[-1 for j in range(1 << n)] for i in range(1000)]

    def F(mask, val):
        if mask == 0:
            return 0
        
        if dp[val][mask] != -1:
            return dp[val][mask]
        
        res = n
        
        if val == 0:
            for i in range(n):
                if mask & (1 << i):
                    res = min(res, F(mask ^ (1 << i), debt[i]))

        
        for i in range(n):
            if mask & (1 << i) and debt[i] * val < 0:
                res = min(res, 1 + F(mask ^ (1 << i), val + debt[i]))

        dp[val][mask] = res

        return res


    return F((1 << n) - 1, 0)
            
