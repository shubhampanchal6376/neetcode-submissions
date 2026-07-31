class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans = []
        a = set()
        b= set()
        for i in nums1:
            if i not in nums2:
                a.add(i)
        for i in nums2:
            if i not in nums1:
                b.add(i)
        ans.append(list(a))
        ans.append(list(b))
        return ans
        