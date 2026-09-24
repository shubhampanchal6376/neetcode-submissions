class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        res = []
        cnt = 0 
        for i in s:
            if i == "(":
                res.append(i)
                cnt+=1
            elif i ==")" and cnt > 0:
                res.append(i)
                cnt-=1
            elif i!=")":
                res.append(i)
        ans = []
        for i in res[::-1]:
            if i == "(" and cnt > 0:
                cnt-=1
            else:
                ans.append(i)
        return "".join(ans[::-1])