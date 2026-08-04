class Solution:
    def sortColors(self, nums: List[int]) -> None:
        ans = []
        r = 0 
        w = 0
        b = 0
        for i in nums:
            if i == 0:
                r+=1
            elif i == 1:
                w+=1
            else:
                b+=1
        for i in range(r):
            ans.append(0)
        for i in range(w):
            ans.append(1)
        for i in range(b):
            ans.append(2)
        nums[:] = ans
        