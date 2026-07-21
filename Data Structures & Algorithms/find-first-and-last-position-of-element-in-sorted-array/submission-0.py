class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first = -1
        last = -1
        n = len(nums)
        s = 0
        e = n-1
        while s<=e:
            mid = s + (e-s)//2
            if nums[mid] == target:
                first = mid
                e = mid-1
            elif nums[mid]<target:
                s = mid+1
            else:
                e = mid -1 
        s = 0
        e = n-1
        while s<=e:
            mid = s + (e-s)//2
            if nums[mid] == target:
                last = mid
                s = mid + 1
            elif nums[mid]<target:
                s = mid+1
            else:
                e = mid - 1
        ans = []
        ans.append(first)
        ans.append(last)
        return ans 