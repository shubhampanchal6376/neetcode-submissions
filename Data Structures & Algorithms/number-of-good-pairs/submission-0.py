class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0 
        n = len(nums)-1
        for i in range(n):
            for j in range(i+1,n+1):
                if nums[i] == nums[j]:
                    ans += 1
        return ans