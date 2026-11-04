class Solution:
    def climbStairs(self, n: int) -> int:
        dp = {}
        def fun(i):
            if i ==n:
                return 1
            if i>n:
                return 0
            if i in dp:
                return dp[i]
            dp[i] = fun(i+1)+fun(i+2)
            return dp[i]
        return fun(0)