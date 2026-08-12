class Solution:
    def merge_array(self , left : List[int] , right : List[int]) -> List[int]:
        res = []
        n,m = len(left),len(right)
        i,j=0,0
        while i<n and j<m:
            if left[i]<=right[j]:
                res.append(left[i])
                i+=1
            else:
                res.append(right[j])
                j+=1
        if i < n:
            while i<n:
                res.append(left[i])
                i+=1
        if j < m:
            while j<m:
                res.append(right[j])
                j+=1
        return res
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums
        mid = len(nums)//2
        left_arr = nums[:mid]
        right_arr = nums[mid:]
        left = self.sortArray(left_arr)
        right = self.sortArray(right_arr)
        return self.merge_array(left,right)