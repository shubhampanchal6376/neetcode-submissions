class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        m = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            if i not in m:
                m[i] = 1
            else:
                m[i] += 1
        for n,v in m.items():
            freq[v].append(n)
        ans = []
        for i in range(len(freq)-1,0,-1):
            for j in freq[i]:
                ans.append(j)
                if len(ans) == k:
                    return ans