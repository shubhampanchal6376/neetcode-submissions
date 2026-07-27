class Solution:
    def reverse(self, x: int) -> int:
        s=""
        t = 0 
        if x == 0 :
            return 0 
        if x<0:
            t = 1
            x = x*(-1)
        while x>0:
            temp = x%10
            s+=str(temp)
            x= x//10
        if t == 0 and int(s) < 2**31 :
            return int(s)
        elif int(s) >= 2**31 :
            return 0
        else:
            return -int(s)