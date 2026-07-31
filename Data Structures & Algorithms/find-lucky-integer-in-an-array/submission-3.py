class Solution:
    def findLucky(self, arr: List[int]) -> int:
        ans = -1
        for i in arr:
            if arr.count(i) == i:
                if i>ans:
                    ans = i
        return ans