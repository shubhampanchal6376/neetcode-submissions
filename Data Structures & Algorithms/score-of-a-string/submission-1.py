class Solution:
    def scoreOfString(self, s: str) -> int:
        a = []
        if len(s) == 1:
            return 0
        for i in s:
            a.append(ord(i))
        sum = abs(a[1]-a[0])
        n = len(a)
        for i in range(2,n):
            sum += abs(a[i]-a[i-1])
        return sum