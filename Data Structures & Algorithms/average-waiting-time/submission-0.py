class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        ans = customers[0][1]
        p = customers[0][0] + customers[0][1]
        n = len(customers)
        for i in range(1,n):
            if p > customers[i][0]:
                ans += p+customers[i][1]-customers[i][0]
                p = p+customers[i][1]
            else:
                ans+=customers[i][1]
                p = customers[i][0]+customers[i][1] 
        return ans/n       