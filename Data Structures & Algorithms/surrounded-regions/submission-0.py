class Solution:
    def solve(self, board: List[List[str]]) -> None:
        def valid(i,j,n,m):
            if i<0 or i>=n or j<0 or j>=m:
                return False
            return True
        x = [-1,1,0,0]
        y = [0,0,-1,1]
        def DFS(board,i,j,n,m):
            board[i][j] = "#"
            for k in range(4):
                row = i+x[k]
                col = j+y[k]
                if valid(row,col,n,m) and board[row][col]=="O":
                    DFS(board,row,col,n,m)
            return 
        n = len(board)
        m = len(board[0])
        for j in range(m):
            if board[0][j]=='O':
                DFS(board,0,j,n,m)
        for j in range(m):
            if board[n-1][j]=="O":
                DFS(board,n-1,j,n,m)
        for i in range(n):
            if board[i][0] =="O":
                DFS(board,i,0,n,m)
        for i in range(n):
            if board[i][m-1]=='O':
                DFS(board,i,m-1,n,m)
        for i in range(n):
            for j in range(m):
                if board[i][j]=='#':
                    board[i][j]='O'
                else:
                    board[i][j]='X'
        return 








