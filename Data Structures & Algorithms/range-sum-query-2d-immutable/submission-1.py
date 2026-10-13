class NumMatrix:
    def __init__(self, matrix: List[List[int]]):
        m, n = len(matrix), len(matrix[0])
        self.p = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(m):
            for j in range(n):
                self.p[i+1][j+1] = (
                    matrix[i][j]
                    + self.p[i+1][j]
                    + self.p[i][j+1]
                    - self.p[i][j]
                )

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return (
            self.p[row2+1][col2+1]
            - self.p[row1][col2+1]
            - self.p[row2+1][col1]
            + self.p[row1][col1]
        )
