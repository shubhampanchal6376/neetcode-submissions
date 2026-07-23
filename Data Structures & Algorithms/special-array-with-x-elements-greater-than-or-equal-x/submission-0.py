class Solution:
    def specialArray(self, nums: List[int]) -> int:
        x = max(nums) + 1
        nums.sort()
        for i in range(0,x):
            l = 0
            r = len(nums)-1
            while l<=r :
                mid = l +(r-l)//2
                if nums[mid] == i:
                    first = mid
                    r = mid - 1
                elif nums[mid] < i:
                    l = mid+1
                else:
                    r = mid-1
                    first = mid
            if len(nums[first:]) == i:
                return i
        return -1

