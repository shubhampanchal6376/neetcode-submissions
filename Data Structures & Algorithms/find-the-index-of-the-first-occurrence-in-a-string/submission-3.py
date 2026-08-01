class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle not in haystack:
            return -1
        l = 0 
        r = len(needle)
        n = len(needle)
        m = len(haystack)
        for i in range(0 ,m-n+1):
            if haystack[l:r] == needle:
                return l
            else:
                l+=1
                r+=1
        return -1
        