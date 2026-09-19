from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        def valid(i,j):
            if i<0 or j<0 or (i+1)>n or (j+1)>m:
                return False
            return True
        q = deque()
        n = len(grid)
        m = len(grid[0])
        fresh = 0 
        time = 0 
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append([i,j])
                    grid[i][j]= -2
                elif grid[i][j] == 1:
                    fresh+=1
        while len(q)>0 and fresh>0:
            s = len(q)
            time += 1
            while s>0:
                a = q[0]
                q.popleft()
                r = a[0]
                c = a[1]
                for k in range(4):
                    row = r + x[k]
                    col = c + y[k]
                    if valid(row,col) and grid[row][col] == 1:
                        q.append([row,col])
                        fresh-=1
                        grid[row][col] = -2
                s-=1
        if fresh>0:
            return -1
        return time