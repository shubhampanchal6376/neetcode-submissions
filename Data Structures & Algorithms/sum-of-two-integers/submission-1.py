class Solution:
    def getSum(self, a: int, b: int) -> int:
        if a>0:
            x = [1]*a
        elif a<0:
            x = [-1]*abs(a)
        else:
            return b
        if b>0:
            y = [1]*b
        elif b<0:
            y = [-1]*abs(b)
        else:
            return a

        ans = []
        for i in x:
            ans.append(i)
        for i in y:
            ans.append(i)
        return sum(ans)