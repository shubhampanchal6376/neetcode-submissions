class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        a = []
        for i in arr:
            if arr.count(i)==1:
                a.append(i)
        if k > len(a):
            return ""
        return a[k-1]