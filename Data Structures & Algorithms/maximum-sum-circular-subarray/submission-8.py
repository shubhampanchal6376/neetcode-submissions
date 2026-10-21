class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        a = nums[0]
        maxsum = nums[0]
        for i in range(1,len(nums)):
            a = max(a+nums[i],nums[i])
            maxsum = max(maxsum,a)
        b = nums[0]
        minsum = nums[0]
        for i in range(1,len(nums)):
            b = min(b+nums[i],nums[i])
            minsum = min(minsum,b)
        s = sum(nums)
        if s!=minsum:
            return max(maxsum,s-minsum)
        else:
            return maxsum