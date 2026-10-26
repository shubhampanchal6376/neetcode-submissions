class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        minp = nums[0]
        maxp = nums[0]
        for i in range(1,len(nums)):
            minp,maxp = min(nums[i],nums[i]*minp,nums[i]*maxp),max(nums[i],nums[i]*minp,nums[i]*maxp)
            ans = max(ans,minp,maxp)
        return ans