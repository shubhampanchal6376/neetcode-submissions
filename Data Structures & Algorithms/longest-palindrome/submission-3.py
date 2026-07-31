class Solution:
    def longestPalindrome(self, s: str) -> int:
        a = 0 
        for i in set(s):
            if s.count(i)%2==0:
                a+=s.count(i)
            else:
                d = s.count(i)-1
                a+=d
        for i in set(s):
            if s.count(i)%2!=0:
                a+=1
                break
        return a