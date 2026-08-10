class Solution:
    def hammingWeight(self, n: int) -> int:
        b = ""
        while n>0:
            b = str(n%2) + b
            n//=2
        cnt = 0 
        for i in b:
            if i == "1":
                cnt+=1
        return cnt