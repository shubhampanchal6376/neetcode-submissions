class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        m = [0]*n
        m[0] = cost[0]
        m[1] = cost[1]
        for i in range(2,n):
            m[i] = min(m[i-1],m[i-2]) + cost[i]
        return min(m[n-1],m[n-2])