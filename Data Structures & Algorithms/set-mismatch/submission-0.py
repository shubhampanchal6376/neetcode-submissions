class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        a = []
        x = 0
        for i in nums:
            if nums.count(i)==2:
                a.append(i)
                x= i
                break
        for i in range(1,len(nums)+1):
            if i not in nums:
                a.append(i)
                break
        return a
        