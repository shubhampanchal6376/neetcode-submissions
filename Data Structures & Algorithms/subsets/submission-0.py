class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        total = 1<<n
        ans = []
        for i in range(total):
            l = []
            for j in range(n):
                if i&(1<<j)!=0:
                    l.append(nums[j])
            ans.append(l)
        return ans