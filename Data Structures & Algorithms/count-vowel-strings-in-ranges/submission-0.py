class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        ans = []
        c = ["a","e","i","o","u"]
        for i in queries:
            l = i[0]
            r = i[1]+1
            x = words[l:r]
            cnt = 0 
            for i in x:
                if i[0] in c and i[-1] in c:
                    cnt+=1
            ans.append(cnt)
        return ans