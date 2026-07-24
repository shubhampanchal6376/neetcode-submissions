class Solution:
    def countSeniors(self, details: List[str]) -> int:
        cnt = 0 
        for i in details:
            l = int(i[11:13])
            if l>60:
                cnt+=1
        return cnt