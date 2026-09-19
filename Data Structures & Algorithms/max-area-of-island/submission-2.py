class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        ans = 0
        def valid(i,j,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        def DFS(grid,n,m,i,j,vis):
            nonlocal ans
            ans+=1
            vis[i][j] = 1
            for k in range(4):
                row = i + x[k]
                col = j + y[k]
                if valid(row,col,n,m) and grid[row][col] == 1 and vis[row][col] == 0:
                    DFS(grid,n,m,row,col,vis)
            return 
        n = len(grid)
        m = len(grid[0])
        res = 0 
        vis = [[0 for _ in range(m)] for _ in range(n)]
        p = []
        for i in range(n):
            for j in range(m):
                if grid[i][j]== 1 and vis[i][j] == 0:
                    DFS(grid,n,m,i,j,vis)
                    p.append(ans-sum(p))
                    res+=1
        if len(p) == 0:
            return 0
        return max(p)