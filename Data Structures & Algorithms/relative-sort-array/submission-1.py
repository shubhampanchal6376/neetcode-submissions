class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        ans = []
        for i in arr2:
            for j in range(arr1.count(i)):
                ans.append(i)
        b = []
        for i in set(arr1):
            if i not in arr2:
                for j in range(arr1.count(i)):
                    b.append(i)
        b.sort()
        for i in b:
            ans.append(i)
        return ans