class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        def dfs(node,parent):
            nonlocal cycle
            vis[node] = 1
            for j in range(len(a[node])):
                neigh = a [node][j]
                if vis[neigh] == 1 and neigh != parent:
                    cycle = True
                if vis[neigh] == 0:
                    dfs(neigh,node)
            return
        a = [[]for _ in range(n)]
        for i in edges:
            s = i[0]
            e = i[1]
            a[s].append(e)
            a[e].append(s)
        vis = [0]*n
        cycle = False
        dfs(0,-1)
        if 0 in vis:
            return False
        if cycle:
            return False
        return True
