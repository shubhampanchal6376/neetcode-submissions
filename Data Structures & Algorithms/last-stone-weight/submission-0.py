class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        a = stones[:]
        while len(a)>1:
            a.sort()
            x = a[-1]
            y = a[-2]
            del a[-2:]
            g = abs(x-y)
            a.append(g)
        return a[0]