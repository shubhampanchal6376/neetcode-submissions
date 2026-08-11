class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        ans = []
        cnt = 1
        # for strictly increasing 
        for i in range(len(nums)-1):
            if nums[i+1]>nums[i]:
                cnt+=1
            else:
                ans.append(cnt)
                cnt = 1
        ans.append(cnt)
        # for strictly decreasing 
        cnt = 1 
        for i in range(1,len(nums)):
            if nums[i]<nums[i-1]:
                cnt+=1
            else:
                ans.append(cnt)
                cnt = 1
        ans.append(cnt)
        return max(ans)