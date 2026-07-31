class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        cnt = 0 
        ans = []
        for i in nums:
            if i == 0:
                cnt+=1
            else:
                ans.append(i)
        for i in range(cnt):
            ans.append(0)
        nums[:] = ans