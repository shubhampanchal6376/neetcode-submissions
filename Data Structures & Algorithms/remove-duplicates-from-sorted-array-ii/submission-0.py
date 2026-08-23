class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        ans = []
        for i in nums:
            if ans.count(i)<2:
                ans.append(i)
        nums[:] = ans
        return len(nums)