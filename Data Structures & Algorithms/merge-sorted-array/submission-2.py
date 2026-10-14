class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i = 0 
        j = 0
        ans = [0]*(m+n)
        id = 0 
        while i<m and j<n:
            if nums1[i]<nums2[j]:
                ans[id] = nums1[i]
                i+=1
                id+=1
            else:
                ans[id] = nums2[j]
                j+=1
                id+=1
        if i==m and j!=n:
            while j<n:
                ans[id]=nums2[j]
                j+=1
                id+=1
        if i!=m and j==n:
            while i<m:
                ans[id]=nums1[i]
                i+=1
                id+=1
        nums1[:] = ans