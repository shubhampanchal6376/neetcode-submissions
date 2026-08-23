class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        r = len(matrix)
        m = [[0]*r for _ in range(r)]
        for i in range(r):
            for j in range(r):
                m[j][r-i-1]=matrix[i][j]
        matrix[:] = m