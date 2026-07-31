class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        a = sum(nums)
        b = set()
        for i in nums:
            b.add(i)
        c = sum(b)
        return 2*c-a