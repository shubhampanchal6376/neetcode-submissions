class Solution:
    def helper(self, nums: List[int], target: int , n : int , diary :list[int], ans:list[int] , idx:int , sum:int):
        if sum==target:
            ans.append(diary.copy())
            return 
        if idx==n:
            return 
        self.helper(nums,target,n,diary,ans,idx+1,sum)
        if sum+nums[idx]<=target:
            diary.append(nums[idx])
            sum+=nums[idx]
            self.helper(nums,target,n,diary,ans,idx,sum)
            diary.pop()
            sum-=nums[idx]
        return 
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        ans = []
        diary = []
        sum = 0 
        idx = 0 
        self.helper(nums,target,n,diary,ans,idx,sum)
        return ans