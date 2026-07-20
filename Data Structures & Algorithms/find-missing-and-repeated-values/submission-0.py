class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        arr = []
        ans = []
        for i in grid:
            for j in i:
                arr.append(j)
        for i in arr:
            if arr.count(i)==2:
                ans.append(i)
                break
        for i in range(len(arr)):
            if (i+1) not in arr:
                ans.append(i+1)  
        return ans          