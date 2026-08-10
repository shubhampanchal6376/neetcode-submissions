class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = [] 
        ans.append(0)
        if n == 0 :
            return ans
        for i in range(1,n+1):
            cnt = 0
            while i>=1:
                t = i%2
                if t == 1:
                    cnt+=1
                i//=2
            ans.append(cnt)
        return ans