class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # Shell_Sort
        gap = len(nums)//2
        while gap > 0:
            for i in range(gap , len(nums)):
                temp = nums[i]
                j = i
                while j>=gap and nums[j-gap]>temp:
                    nums[j] = nums[j-gap]
                    j-=gap
                nums[j] = temp
            gap//=2
        return nums