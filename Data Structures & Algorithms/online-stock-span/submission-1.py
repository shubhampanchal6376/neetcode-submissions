class StockSpanner:

    def __init__(self):
        self.s = []

    def next(self, price: int) -> int:
        cnt = 1 
        self.s.append(price)
        x = self.s[::-1]
        for i in range(1,len(x)):
            if x[i]<=price:
                cnt+=1
                continue
            else:
                break
        return cnt
            
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)