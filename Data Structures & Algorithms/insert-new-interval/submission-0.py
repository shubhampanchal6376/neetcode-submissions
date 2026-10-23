class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        ans = []
        s1 = intervals[0][0]
        e1 = intervals[0][1]
        for i in range(1,len(intervals)):
            s2 = intervals[i][0]
            e2 = intervals[i][1]
            if e1>=s2:
                s1 = s1
                e1 = max(e1,e2)
                continue
            ans.append([s1,e1])
            s1 = s2
            e1 = e2
        ans.append([s1,e1])
        return ans