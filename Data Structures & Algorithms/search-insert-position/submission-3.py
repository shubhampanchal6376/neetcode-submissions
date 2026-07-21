class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        index = len(nums)
        l = 0 
        r = index -1 
        while l <= r:
            mid = l + (r-l)//2
            if nums[mid] == target:
                index = mid
                break
            elif nums[mid] < target : 
                l = mid + 1
            else:
                r = mid -1
                index = mid
        return index