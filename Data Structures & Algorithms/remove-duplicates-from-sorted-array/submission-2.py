class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        off = 0 
        res = 1
        cur = 1
        n = len(nums)
        while cur<n:
            if nums[cur]==nums[cur-1]:
                cur+=1
                continue
            else:
                nums[off+1]=nums[cur]
                cur+=1
                res+=1
                off+=1
        return res

        