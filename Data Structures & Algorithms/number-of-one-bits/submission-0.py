class Solution:
    def hammingWeight(self, n: int) -> int:
        b = bin(n)
        s = str(b)
        cnt = 0 
        for i in s:
            if i == "1":
                cnt+=1
        return cnt