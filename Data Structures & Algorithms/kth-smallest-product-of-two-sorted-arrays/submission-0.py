class Solution:
    def kthSmallestProduct(self, nums1: List[int], nums2: List[int], k: int) -> int:
        ans = []
        for i in nums1:
            for j in nums2:
                ans.append(i*j)
        ans.sort()
        return ans[k-1]        