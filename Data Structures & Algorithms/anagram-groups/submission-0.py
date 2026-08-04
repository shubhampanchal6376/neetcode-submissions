class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        d = {}
        for i in strs:
            key = "".join(sorted(i))
            if key not in d:
                d[key] =  []
            d[key].append(i)
        for i in d.values():
            ans.append(i)
        return ans