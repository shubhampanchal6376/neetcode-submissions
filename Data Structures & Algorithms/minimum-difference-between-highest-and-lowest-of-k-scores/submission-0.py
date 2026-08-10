class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = nums[:]
        ans = max(nums)
        for i in range(len(nums)-k+1):
            m = nums[i+k-1] - nums[i]
            ans = min(ans,m)
        return ans