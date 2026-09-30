class Solution:
    def isHappy(self, n: int) -> bool:
        def fun(n):
            sum = 0  
            while n>0:
                temp = n%10
                sum+=temp**2
                n = n//10
            return sum
        slow = n
        fast = n
        while fast!=1:
            slow = fun(slow)
            fast = fun(fun(fast))
            if slow == fast and slow != 1:
                return False
        return True
        