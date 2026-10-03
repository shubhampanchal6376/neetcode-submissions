class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        a = nums[0]
        p = nums[0]
        for i in range(1,len(nums)):
            a = max(nums[i],a+nums[i])
            p = max(a,p)
        b = nums[0]
        q = nums[0]
        for i in range(1,len(nums)):
            b = min(nums[i],b+nums[i])
            q = min(b,q)
        s = sum(nums)
        if s!=q:
            return max(p,s-q)
        else:
            return p