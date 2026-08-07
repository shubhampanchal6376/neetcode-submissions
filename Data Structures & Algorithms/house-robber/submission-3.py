class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        a,b = 0,0
        for i in nums:
            temp = max(a,b+i)
            b = a
            a = temp
        return a