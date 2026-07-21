class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        if sum(nums) == 0 and len(nums)>=2:
            return True
        if len(nums)<2:
            return False
        if sum(nums)<k:
            return False
        left = 0 
        right = 1
        n = len(nums)
        while left < right :
            s = sum(nums[left:right+1])
            if s%k == 0 :
                return True 
            elif right == n-1:
                left+=1
            else:
                right+=1
        return False     
