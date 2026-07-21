class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        a = list(s)
        b = list(t)
        for i in b:
            if i == a[0]:
                a.pop(0)
            if len(a) == 0 :
                break
        return len(a) == 0