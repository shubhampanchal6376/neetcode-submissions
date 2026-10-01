class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        low = 0
        ans = 0 
        p = 1
        n = len(nums)
        if k<=1:
            return 0
        for high in range(n):
            p = p*nums[high]
            while p>=k:
                if low>high:
                    break
                p = p//nums[low]
                low+=1
            if low<=high:
                ans+=high-low+1
        return ans
            
            