class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = []
        s = []
        a = 1
        for i in nums:
            a = a*i
            p.append(a)
        b = 1
        for i in nums[::-1]:
            b = b*i
            s.append(b)
        s = s[::-1]
        for i in range(len(nums)):
            if i==0:
                nums[i] = s[i+1]
            elif i==len(nums)-1:
                nums[i] = p[i-1]
            else:
                nums[i] = p[i-1]*s[i+1]
        return nums