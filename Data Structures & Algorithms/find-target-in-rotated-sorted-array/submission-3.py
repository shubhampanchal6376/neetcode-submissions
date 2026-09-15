class Solution:
    def search(self, nums: List[int], target: int) -> int:
        s = 0 
        e = len(nums)
        while s<e:
            mid = (s+e)//2
            if nums[mid] == target:
                return mid
            if nums[s]<=nums[mid]:
                if nums[s] <= target < nums[mid]:
                    e = mid
                else:
                    s = mid + 1
            else:
                if nums[mid] < target <= nums[e-1]:
                    s = mid + 1
                else:
                    e = mid
        return -1