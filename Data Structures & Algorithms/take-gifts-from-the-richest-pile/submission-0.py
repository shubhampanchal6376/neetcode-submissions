class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        n = k
        while n>0:
            gifts.sort()
            x = gifts[-1]
            del gifts[-1:]
            gifts.append(int(sqrt(x)))
            n-=1
        return sum(gifts)

