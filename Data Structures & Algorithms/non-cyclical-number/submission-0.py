class Solution:
    def helper(eslf, n : int ) -> int:
        sum = 0
        while n>0:
            temp = n%10
            sum+=temp*temp
            n = n//10
        return sum     
    def isHappy(self, n: int) -> bool:
        seen = []
        while n==1 or n not in seen:
            if n == 1:
                return True 
            else:
                seen.append(n)
                n = self.helper(n)
        return False