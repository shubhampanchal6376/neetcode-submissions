class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        r = len(matrix)
        c = len(matrix[0])
        m = [[0]*r for _ in range(c)]
        for i in range(c):
            for j in range(r):
                m[i][j] = matrix[j][i]
        return m