import math 
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        ans = 0
        for i in digits:
            ans = ans*10 + i
        ans+=1
        a = [int(x) for x in str(ans)]
        return a