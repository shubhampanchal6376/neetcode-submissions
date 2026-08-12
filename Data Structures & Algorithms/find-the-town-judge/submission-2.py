class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        a = trust[0][1]
        if a > n:
            return -1
        b = set()
        for i in trust:
            if i[0] == a:
                return -1
        for i in trust:
            b.add(i[0])
        c = []
        for i in b:
            x = []
            x.append(i)
            x.append(a)
            c.append(x)
        for i in c:
            if i not in trust:
                return -1
        return a
