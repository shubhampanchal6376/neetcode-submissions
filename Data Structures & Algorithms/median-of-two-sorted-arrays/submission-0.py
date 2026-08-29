class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        ans = []
        for i in nums1:
            ans.append(i)
        for i in nums2:
            ans.append(i)
        ans.sort()
        n = len(ans)
        if n%2==0:
            a = n//2
            b = n//2-1
            return (ans[a]+ans[b])/2
        else:
            return ans[n//2]