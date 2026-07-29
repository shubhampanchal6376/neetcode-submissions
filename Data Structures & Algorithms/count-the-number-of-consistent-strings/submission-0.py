class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        cnt = 0 
        for i in words:
            b = 0 
            for j in i : 
                if j in allowed : 
                    b+=1
                else:
                    break
            if b == len(i):
                cnt+=1
        return cnt
            