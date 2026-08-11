class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        cnt = 0 
        n = len(s)
        m = len(t)
        j = -1 
        for i in range(m):
            j+=1
            while j < n:
                if t[i] == s[j]:
                    cnt+=1
                    break
                else:
                    j+=1
                    if j == n:
                        break
            if j == n:
                break
        return m - cnt