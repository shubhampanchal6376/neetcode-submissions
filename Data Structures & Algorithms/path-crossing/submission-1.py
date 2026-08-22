class Solution:
    def isPathCrossing(self, path: str) -> bool:
        a = []
        x = [0,0]
        a.append([0,0])
        for i in path: 
            if i == "N":
                x[0]+=1
            elif i == "S":
                x[0]-=1
            elif i == "E":
                x[1]+=1
            else:
                x[1]-=1
            if x in a:
                return True
            # One-line concept: c = x copies the reference, not the list; use c = x.copy() to create a separate list
            c = x.copy()
            a.append(c)
        return False