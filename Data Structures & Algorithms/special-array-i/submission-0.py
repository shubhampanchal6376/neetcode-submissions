class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        if nums[0]%2==0:
            for i in range(2,len(nums),2):
                if nums[i]%2!=0:
                    return False
                if nums[i-1]%2==0:
                    return False
        else:
            for i in range(2,len(nums),2):
                if nums[i]%2==0:
                    return False
                if nums[i-1]%2!=0:
                    return False
        return True