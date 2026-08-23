class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0 
        r = len(mat)
        j = r-1
        for i in range(r):
            if i == j:
                ans+=mat[i][j]
            else:
                ans+=mat[i][i]+mat[i][j]
            j-=1
        return ans