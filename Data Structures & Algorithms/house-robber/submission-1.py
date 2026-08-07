class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 0 :
            return 0
        if n <= 2:
            return max(nums)
        p = nums[0]
        q = max(nums[0],nums[1])
        for i in range(2,n):
            curr = max(q,nums[i]+p)
            p = q
            q = curr
        return q