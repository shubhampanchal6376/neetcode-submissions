class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        total = 1<<n
        ans = []
        for i in range(total):
            l = []
            for j in range(n):
                if i&(1<<j)!=0:
                    l.append(nums[j])
            ans.append(l)
        a = []
        for i in ans:
            v = 0
            for j in i:
                v = v^j
            a.append(v)
        return sum(a)
        
            