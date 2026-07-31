class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        ans = ""
        for i in t:
            if i not in s:
                return i
            else:
                if (s.count(i)) == (t.count(i))-1:
                    return i 