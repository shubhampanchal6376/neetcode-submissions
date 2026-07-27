class Solution:
    def maxScore(self, s: str) -> int:
        ans = []
        for i in range(1, len(s)):
            a = s[:i]
            b = s[i:]
            x = 0
            y = 0
            for i in a:
                if i == "0":
                    x+=1
            for i in b:
                if i == "1":
                    y+=1
            g = x+y
            ans.append(g)
        if len(ans)==1:
            return ans[0]
        return max(ans)