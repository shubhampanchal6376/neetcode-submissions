class Solution:
    def maxDifference(self, s: str) -> int:
        f1 = []
        f2 = []
        for i in s:
            if s.count(i)%2==0:
                f2.append(s.count(i))
            else:
                f1.append(s.count(i))
        a = max(f1)-min(f2)
        return a