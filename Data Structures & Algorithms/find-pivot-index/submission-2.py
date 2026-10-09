class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left = 0 
        s = sum(nums)
        if 0 == sum(nums[1:]):
            return 0
        for i in range(1,len(nums)):
            left += nums[i-1]
            right = s-nums[i]-left
            if left == right:
                return i 
        return -1