class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        t = 0
        a = 0
        for i in nums:
            if i==1:
                a+=1
            else:
                a = 0
            if a>t:
                t = a
        return t