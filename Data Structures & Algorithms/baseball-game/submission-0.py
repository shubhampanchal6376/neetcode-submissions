class Solution:
    def calPoints(self, operations: List[str]) -> int:
        ans = []
        n = len(operations)
        for i in range(n):
            if operations[i] == "+":
                ans.append(ans[-1]+ans[-2])
            elif operations[i] == "D":
                ans.append(ans[-1]*2)
            elif operations[i] == "C":
                x = ans.pop()
            else:
                ans.append(int(operations[i]))
        return sum(ans)