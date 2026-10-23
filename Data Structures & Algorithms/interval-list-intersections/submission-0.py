class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        ans = []
        i = 0 
        j = 0
        while i<n and j<m :
            s1 = firstList[i][0]
            e1 = firstList[i][1]
            s2 = secondList[j][0]
            e2 = secondList[j][1]
            if s1<s2:
                if e1>=s2:
                    s = max(s1,s2)
                    e = min(e1,e2)
                    ans.append([s,e])
            else:
                if e2 >= s1:
                    s = max(s1,s2)
                    e = min(e1,e2)
                    ans.append([s,e])
            if e1<=e2:
                i+=1
            else:
                j+=1
        return ans
