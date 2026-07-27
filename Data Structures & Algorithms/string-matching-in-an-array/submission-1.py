class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        ans = []
        for i in words:
            for j in range(0,len(words)):
                if i in words[j] and i != words[j]:
                    ans.append(i)
        return list(set(ans))