class Solution:
    def customSortString(self, order: str, s: str) -> str:
        u = []
        for i in s:
            u.append(ord(i))
        u.sort()
        x = ""
        for i in u:
            x+=chr(i)
        a = ""
        for i in order:
            for j in range(x.count(i)):
                a+=i
        for i in x:
            if i not in order:
                a+=i
        return a