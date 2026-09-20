class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        def dfs(node,parent):
            vis[node] = 1
            for j in range(len(a[node])):
                neigh = a[node][j]
                if vis[neigh] == 0:
                    dfs(neigh,node)
            return 
        a = [[]for _ in range(n)]
        vis = [0]*n
        cnt = 0
        for i in edges:
            a[i[0]].append(i[1])
            a[i[1]].append(i[0])
        for i in range(len(vis)):
            if 0 not in vis:
                break
            if vis[i]==0:
                cnt+=1
                dfs(i,-1)
        return cnt