class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = []
        prefix.append(nums[0])
        n = len(nums)
        for i in range(1,n):
            prefix.append(prefix[i-1]*nums[i])
        x = nums[::-1]
        suffix = []
        suffix.append(x[0])
        m = len(x)
        for i in range(1,m):
            suffix.append(suffix[i-1]*x[i])
        suffix = suffix[::-1]
        ans = []
        prefix = [1]+prefix+[1]
        suffix = [1]+suffix+[1]
        for i in range(len(prefix)-2):
            ans.append(prefix[i]*suffix[i+2])
        return ans
