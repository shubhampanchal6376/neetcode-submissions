class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        a = set()
        for i in nums1:
            if i in nums2:
                a.add(i)
        ans = []
        for i in a:
            ans.append(i)
        return ans