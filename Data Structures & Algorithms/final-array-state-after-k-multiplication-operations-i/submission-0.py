class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        n = k
        while n>0:
            x = min(nums)
            for i in range(len(nums)):
                if nums[i] == x:
                    break
            nums[i] = x*multiplier
            n-=1
        return nums