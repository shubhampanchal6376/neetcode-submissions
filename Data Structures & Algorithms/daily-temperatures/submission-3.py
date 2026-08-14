class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = []
        a = temperatures[:]
        n = len(temperatures)
        a.sort(reverse=True)
        if a == temperatures:
            x = [0]*n
            return x
        for i in range(n-1):
            f = 0 
            for j in range(i+1,n):
                if temperatures[j]>temperatures[i]:
                    f = 1
                    ans.append(j-i)
                    break
            if f == 0:
                ans.append(0)
        ans.append(0)
        return ans