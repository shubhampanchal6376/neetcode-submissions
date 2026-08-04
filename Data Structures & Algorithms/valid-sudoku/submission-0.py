class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9 
        r = [0]*n
        c = [0]*n
        box = [0]*n
        for i in range(n):
            r[i] = set()
            c[i] = set()
            box[i] = set()
        for i in range(9):
            for j in range(9):
                cell = board[i][j]
                if cell == ".":
                    continue
                if cell in r[i]:
                    return False
                r[i].add(cell)
                if cell in c[j]:
                    return False
                c[j].add(cell)
                index = 3*(i//3) + j//3
                if cell in box[index]:
                    return False
                box[index].add(cell)
        return True