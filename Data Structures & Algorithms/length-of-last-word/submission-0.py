class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        p = []
        a = ""
        t = 0 
        for i in range(len(s)-1,-1,-1):
            if s[i] == " ":
                t+=1
            else:
                break
        c = len(s)-t
        g = s[:c]
        cnt = 0
        for i in range(len(g)-1,-1,-1):
            if g[i] == " ":
                break
            else:
                cnt+=1
        return cnt 
            
