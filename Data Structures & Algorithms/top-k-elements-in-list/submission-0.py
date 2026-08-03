class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        seen = []
        for i in nums:
            if i in seen:
                mp[i] += 1
            else:
                mp[i] = 1
                seen.append(i)
        ans = []
        m = dict(sorted(mp. items(), key = lambda x:x[1]))
        for i in m.keys():
            ans.append(i)
        return ans[-k:]
             
