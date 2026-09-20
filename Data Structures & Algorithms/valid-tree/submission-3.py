class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(a,node,parent,vis):
            nonlocal cycle
            vis[node] = 1
            for j in range(len(a[node])):
                neigh = a [node][j]
                if vis[neigh] == 1 and neigh != parent:
                    cycle = True
                if vis[neigh] == 0:
                    dfs(a,neigh,node,vis)
            return
        a = [[]for _ in range(n)]
        for i in edges:
            s = i[0]
            e = i[1]
            a[s].append(e)
            a[e].append(s)
        vis = [0]*n
        cycle = False
        for i in range(n):
            if vis[i] == 0 :
                dfs(a,0,-1,vis)
        if cycle:
            return False
        return True
