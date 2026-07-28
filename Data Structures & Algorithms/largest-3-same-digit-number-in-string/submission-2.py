class Solution:
    def largestGoodInteger(self, num: str) -> str:
        ans = []
        s = ""
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                s = num[i]+num[i+1]+num[i+2]
                ans.append(s)
        if len(ans)==0:
            return ""
        else:
            return max(ans) 