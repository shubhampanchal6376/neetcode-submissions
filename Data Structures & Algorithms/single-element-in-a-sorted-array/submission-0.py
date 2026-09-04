class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        s = set(nums)
        a = sum(s)
        b = sum(nums)
        return 2*a-b