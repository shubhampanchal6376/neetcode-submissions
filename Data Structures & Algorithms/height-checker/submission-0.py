class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        cnt = 0 
        arr = heights[:]
        arr.sort()
        for i in range(len(arr)):
            if arr[i] != heights[i]:
                cnt+=1
        return cnt