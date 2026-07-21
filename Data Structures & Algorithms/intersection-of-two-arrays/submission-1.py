class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        seen = set(nums1)
        seens = set(nums2)
        return [num for num in seen if num in seens]
