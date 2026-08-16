class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        for i in nums:
            if i>=0:
                p.append(i)
            else:
                n.append(i)
        ans = []
        c = len(nums)//2
        for i in range(c):
            ans.append(p[i])
            ans.append(n[i])
        return ans