class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        su = n*(n+1)/2
        add = sum(nums)
        if su == add:
            return 0
        else:
            return int(su - add)
