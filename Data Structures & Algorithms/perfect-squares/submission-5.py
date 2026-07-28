class Solution:
    def numSquares(self, n: int) -> int:
        ans = []
        i = 1
        cnt=0
        sum = []
        a = n
        if n==1:
            return 1
        while i <= n//2 :
            if i**2 <= n:
                ans.append(i**2)
            i+=1
        t = []
        while len(ans)>0:
            n = a
            cnt = 0 
            for i in ans[::-1]:
                while i<=n:
                    n-=i
                    cnt+=1
            if n==0:
                t.append(cnt)
            ans.pop()
        return min(t)
        
                