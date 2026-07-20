class Solution:
    def isPalindrome(self, x: int) -> bool:
        a = x
        r = 0 
        while a>0:
            temp = a%10
            r = r*10 + temp
            a = a//10
        return r==x