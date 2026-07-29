class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        a = dict()
        for i in range(0,len(heights)):
                a[heights[i]] = names[i]
        b = dict(sorted(a.items()))
        t = []
        for i in b.values():
            t.append(i)
        return t[::-1]