class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        cnt = 0 
        i = 0 
        n = len(tickets)
        while tickets[k] > 0:
            if tickets[i] != 0:
                tickets[i] -=1
                cnt+=1
            i+=1
            if i == n:
                i = 0
        return cnt