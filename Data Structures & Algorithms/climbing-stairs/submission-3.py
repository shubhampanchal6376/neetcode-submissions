class Solution:
    m = {}
    def climbStairs(self, n: int) -> int:
        if n in self.m:
            return self.m[n]
        if n<=2 :
            return n
        result = self.climbStairs(n-1)+self.climbStairs(n-2)
        self.m[n] = result
        return result