class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        ans = []
        m = {}
        nums.sort(reverse = True)
        for i in nums:
            if i in m:
                m[i]+=1
            else:
                m[i] = 1
        s = dict(sorted(m.items(), key=lambda x: x[1]))
        for i,j in s.items():
            for b in range(j):
                ans.append(i)
        return ans