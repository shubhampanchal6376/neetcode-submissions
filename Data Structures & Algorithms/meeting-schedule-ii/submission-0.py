"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        s = []
        e = []
        n = len(intervals)
        for i in intervals:
            s.append(i.start)
            e.append(i.end)
        s.sort()
        e.sort()
        i = 0 
        j = 0
        room = 0
        ans = 0 
        while i<n and j<n:
            if s[i]<e[j]:
                room+=1
                ans = max(ans,room)
                i+=1
            else:
                room-=1
                j+=1
        return ans