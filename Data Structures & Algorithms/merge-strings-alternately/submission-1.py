class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        x = ""
        for i , j in zip(word1,word2):
            x+=i
            x+=j
        x += word2[len(word1):]
        x += word1[len(word2):]
        return x