class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        inserted = False
        for i in range(len(intervals)):
            if not inserted and newInterval[0] <= intervals[i][0]:
                res.append(newInterval)
                inserted = True

            res.append(intervals[i])

        if not inserted:
            res.append(newInterval)

        # Merge overlapping intervals
        ans = []
        s1 = res[0][0]
        e1 = res[0][1]

        for i in range(1, len(res)):
            s2 = res[i][0]
            e2 = res[i][1]

            if e1 >= s2:
                e1 = max(e1, e2)
                continue

            ans.append([s1, e1])
            s1 = s2
            e1 = e2

        ans.append([s1, e1])

        return ans
    
