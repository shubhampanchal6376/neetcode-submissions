class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        ans = nums[0]
        maxp = nums[0]
        minp = nums[0]
        for i in range(1,len(nums)):
            v1 = nums[i]
            v2 = maxp*nums[i]
            v3 = minp*nums[i]
            maxp = max(v1,v2,v3)
            minp = min(v1,v2,v3)
            ans = max(ans,maxp,minp)
        return ans