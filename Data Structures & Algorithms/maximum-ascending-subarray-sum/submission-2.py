class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        x = []
        sum = nums[0] 
        a = 0 
        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                a = 1
                sum+=nums[i]
            else:
                x.append(sum)
                sum = nums[i]
        x.append(sum)
        if a==0 :
            return nums[0]
        else:
            return max(x)
        
        