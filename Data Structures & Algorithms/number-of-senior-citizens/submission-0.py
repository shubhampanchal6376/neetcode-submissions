class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0 
        for i in details:
            a = i[11:13]
            l = int(a)
            if l>60:
                cnt+=1
        return cnt