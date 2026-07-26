class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        s = []
        for i in strs:
            s.append(len(i))
        m = min(s)
        a = ""
        for i in strs:
            if len(i) == m:
                a+=i
        n = len(strs)
        t = ""
        for i in strs:
            ans+=i
        for i in a:
            if ans.count(t+i) >= n :
                t+=i
            else:
                break
        return t