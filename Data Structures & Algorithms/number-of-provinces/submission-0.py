class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node,parent):
            vis[node] = 1
            for i in range(len(a[node])):
                neigh = a[node][i]
                if vis[neigh] == 0:
                    dfs(neigh,node)
            return 
        n = len(isConnected)
        a = [[]for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if isConnected[i][j] == 1:
                    a[i].append(j)
                    a[j].append(i)
        vis = [0]*n
        cnt = 0
        for i in range(len(vis)):
            if 0 not in vis:
                break
            if vis[i] == 0:
                cnt+=1
                dfs(i,-1)
        return cnt