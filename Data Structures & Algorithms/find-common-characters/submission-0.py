class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        x = words[0]
        ans = []
        s = set()
        for i in x:
            s.add(i)
        for i in s:
            x = words[0].count(i) 
            for j in words:
                if x>j.count(i):
                    x = j.count(i)
            for b in range(x):
                ans.append(i)
        return ans
        