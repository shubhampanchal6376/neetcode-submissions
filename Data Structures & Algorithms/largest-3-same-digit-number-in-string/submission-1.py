class Solution:
    def largestGoodInteger(self, num: str) -> str:
        cnt = 1 
        ans = []
        for i in range(1,len(num)):
            if num[i] == num[i-1]:
                cnt+=1
            else:
                cnt = 1 
            if cnt == 3:
                s = ""
                s = s + num[i] + num[i-1] + num[i-2]
                ans.append(s)
        if len(ans) == 0 :
            return ""
        else:
            return max(ans)
        