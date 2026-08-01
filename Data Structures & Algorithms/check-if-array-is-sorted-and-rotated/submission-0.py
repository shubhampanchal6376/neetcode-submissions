class Solution:
    def check(self, nums: List[int]) -> bool:
        a = nums[:]
        a.sort()
        n = len(a)
        x = nums.index(a[0])
        for i in range(0,n):
            if a[i] != nums[(i+x)%n]:
                return False
        return True