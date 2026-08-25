class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        cnt = 0 
        s = len(words)
        for i in range(s):
            n = len(words[i])
            for j in range(i+1,s):
                if len(words[j])>=n and words[i] == words[j][:n] and words[i] == words[j][-n:]:
                    cnt+=1
        return cnt