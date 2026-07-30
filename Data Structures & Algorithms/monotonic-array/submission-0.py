class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        x = nums[:]
        y = nums[:]
        y.sort()
        z = y[::-1]

        return x == y or x == z 