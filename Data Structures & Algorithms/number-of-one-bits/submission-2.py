class Solution:
    def hammingWeight(self, n: int) -> int:
        cnt = 0 
        while n>=1:
            t = n%2
            if t == 1:
                cnt+=1
            n//=2
        return cnt