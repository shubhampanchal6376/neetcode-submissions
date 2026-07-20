class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        a = nums[n-1]*nums[n-2] - nums[1]*nums[0]
        return a 