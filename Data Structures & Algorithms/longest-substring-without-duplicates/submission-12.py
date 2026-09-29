class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        low = 0
        ans = 0
        m = {}
        for high in range(len(s)):
            m[s[high]] = m.get(s[high],0)+1
            k = high - low +1
            while len(m)<k:
                m[s[low]]-=1
                if m[s[low]]==0:
                    del m[s[low]]
                low+=1
                k = high-low+1
            ans = max(ans,high-low+1)
        return ans

