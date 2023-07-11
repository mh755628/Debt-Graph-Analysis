#include <bits/stdc++.h>
using namespace std;

template <class TF, class TC, TF Foo, TC Coo>
struct
    MinCostMaximumFlow
{
    static const int MAXV = 1e5 + 5;
    static const int MAXE = 1e6 + 5;
    int n, s, t, E;
    int adj[MAXE], nxt[MAXE], lst[MAXV], frm[MAXV], vis[MAXV];
    TF cap[MAXE], flw[MAXE], totalFlow;
    TC cst[MAXE], dst[MAXV], totalCost;
    void init(int n, int s, int t)
    {
        this->n = n, this->s = s, this->t = t;
        fill_n(lst, n, -1), E = 0;
    }
    void add(int u, int v, TF ca, TC co)
    {
        adj[E] = v, cap[E] = ca, flw[E] = 0, cst[E] = +co,
        nxt[E] = lst[u], lst[u] = E++;
        adj[E] = u, cap[E] = 0, flw[E] = 0, cst[E] = -co, nxt[E] = lst[v], lst[v] = E++;
    }
    int spfa()
    {
        fill_n(dst, n, Coo), dst[s] = 0;
        queue<int> que;
        que.push(s);
        while (que.size())
        {
            int u = que.front();
            que.pop();
            for (int e = lst[u]; e != -1; e = nxt[e])
                if (flw
                        [e] < cap[e])
                {
                    int v = adj[e];
                    if (dst[v] > dst[u] + cst[e])
                    {
                        dst[v] = dst[u] + cst[e];
                        frm[v] = e;
                        if (!vis[v])
                        {
                            vis[v] = 1;
                            que.push(v);
                        }
                    }
                }
            vis[u] = 0;
        }
        return dst[t] < Coo;
    }
    TC mincost()
    {
        totalCost = 0, totalFlow = 0;
        while (1)
        {
            if (!spfa())
                break;
            TF mn = Foo;
            for (int v = t, e = frm[v]; v != s; v = adj[e ^
                                                        1],
                     e = frm[v])
                mn = min(mn, cap[e] - flw[e]);
            for (int v = t, e = frm[v]; v != s; v = adj[e ^
                                                        1],
                     e = frm[v])
            {
                flw[e] += mn;
                flw[e ^ 1] -= mn;
            }
            totalFlow += mn;
            totalCost += dst[t];
        }
        return totalCost;
    }
};
MinCostMaximumFlow<int, int, (int)1e9, (int)1e9> mcmf;
int main()
{
    // int test, tc = 0;
    // cin >> test;
    // while (test--)
    // {
    //     int n;
    //     cin >> n;
    //     mcmf.init(2 * n + 2, 0, 2 * n + 1);
    //     // MCMF G(0, 2 * n + 1, 2 * n + 2);
    //     for (int i = 1; i <= n; i++)
    //     {
    //         for (int j = 1; j <= n; j++)
    //         {
    //             int x;
    //             cin >> x;
    //             mcmf.add(i, j + n, 1, -x);
    //         }
    //     }
    //     for (int i = 1; i <= n; i++)
    //     {
    //         mcmf.add(0, i, 1, 0);
    //         mcmf.add(i + n, 2 * n + 1, 1, 0);
    //     }
    //     cout << "Case " << ++tc << ": " << -mcmf.mincost() << endl;
    // }

    //read input.txt


    // freopen("input.txt", "r", stdin);

    int n, m; cin >> n >> m;

    cout << n << " " << m << endl;

    vector <int> debt(n + 1, 0);

    for(int i = 0; i < m; i++) {
        int u, v, w; cin >> u >> v >> w;
        cout << u << " " << v << " " << w << endl;
        debt[u] += w;
        debt[v] -= w;
    }

    for(int i = 0; i < n; i++) if(debt[i] != 0) {
        cout << debt[i] << " ";
    }

    cout << endl;

    vector <int> in_debt, in_cred;

    mcmf.init(n + 2, n, n + 1);

    for(int i = 0; i < n; i++) {
        if(debt[i] > 0) {
            mcmf.add(n, i, debt[i], 0);
            in_debt.push_back(i);
        }
        else if(debt[i] < 0) {
            in_cred.push_back(i);
            mcmf.add(i, n + 1, -debt[i], 0);
        }
    }

    for(int i = 0; i < in_debt.size(); i++) {
        for(int j = 0; j < in_cred.size(); j++) {
            mcmf.add(in_debt[i], in_cred[j], 1e9, 1);
        }
    }

    cout << mcmf.mincost() << endl;

    //find all the edges

    for (int i = 0; i < mcmf.E; i += 2)
    {
        if (mcmf.flw[i] > 0 and mcmf.adj[i] != n and mcmf.adj[i ^ 1] != n + 1)
        {
            cout << mcmf.adj[i] << " " << mcmf.adj[i ^ 1] << " " << mcmf.flw[i] << endl;
        }
    }
}