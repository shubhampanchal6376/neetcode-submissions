class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        def valid(i,j):
            if i<0 or j<0 or i>n-1 or j>m-1:
                return False
            return True
        def dfs(image,n,m,i,j,vis):
            vis[i][j] = 1
            image[i][j] = color 
            for k in range(4):
                row = i + x[k]
                col = j + y[k]
                if valid(row,col) and vis[row][col] == 0 and image[row][col] == p:
                    dfs(image,n,m,row,col,vis)
            return 
        n = len(image)
        m = len(image[0])
        vis = [[0 for _ in range(m)] for _ in range(n)]
        p = image[sr][sc]
        if p == color:
            return image
        dfs(image,n,m,sr,sc,vis)
        return image

        