class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if target in triplets:
            return True
        a = []
        for i in triplets:
            if i[0]<=target[0] and i[1]<=target[1] and i[2]<=target[2]:
                a.append(i)
        if len(a)==0:
            return False
        x = a[0][0]
        y = a[0][1]
        z = a[0][2]
        for i in range(1,len(a)):
            x = max(x,a[i][0])
            y = max(y,a[i][1])
            z = max(z,a[i][2])
            if x==target[0] and y == target[1] and z == target[2]:
                return True
        return False