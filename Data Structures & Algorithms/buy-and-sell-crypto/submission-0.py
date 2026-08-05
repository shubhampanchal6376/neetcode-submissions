class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = []
        x = sorted(prices)
        if prices == x[::-1]:
            return 0
        for i in range(len(prices)-1):
            x = prices[i+1:]
            ans.append(max(x)-prices[i])
        return max(ans)