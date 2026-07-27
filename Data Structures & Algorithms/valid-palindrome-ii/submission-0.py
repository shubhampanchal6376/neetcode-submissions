class Solution:
    def validPalindrome(self, s: str) -> bool:
        t = s[:]
        n = len(s)
        if t == t[::-1]:
            return True
        a= 0 
        for i in range(n):
            if t[i] == t[n-i-1]:
                continue
            else:
                new = ""
                w = ""
                a = 1
                if a == 1:
                    new += t[:i] + t[i+1:]
                    if new == new[::-1]:
                        return True
                    else:
                        a = 2
                if a == 2:
                    w += t[:n-i-1] + t[n-i:]
                    if w == w[::-1]:
                        return True
                    else:
                        a = 3
                if a == 3 :
                    return False
        return True