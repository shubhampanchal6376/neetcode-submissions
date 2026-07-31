class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        m = dict()
        ans = []
        for i in nums1:
            m[i] = 1
        for i in nums2:
            if i in m and m.get(i) == 1:
                m[i] = 0 
                ans.append(i)
        return ans
