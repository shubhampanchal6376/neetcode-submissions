class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        a = money
        if len(prices) == 1:
            money-=(prices[0]*2)
            if money >= 0:
                return money
            else:
                return a
        for i in range(2):
            money-=prices[i]
        if money>=0:
            return money
        else:
            return a
        