class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        l = 0
        r = 0 
        cnt = 0 
        n = len(nums)
        sum = 0 
        while l<n:
            sum += nums[r]
            if sum==goal:
                cnt+=1
            r+=1
            if r==n:
                sum = 0 
                l+=1
                r = l
        return cnt