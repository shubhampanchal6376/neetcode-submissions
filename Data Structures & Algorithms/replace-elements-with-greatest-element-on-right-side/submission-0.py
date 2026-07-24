class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        a = []
        for i in range(len(arr)-1):
            m = max(arr[i+1:])
            a.append(m)
        a.append(-1)
        return a