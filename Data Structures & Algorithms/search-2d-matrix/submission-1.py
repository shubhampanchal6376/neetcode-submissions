class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])
        l = 0 
        r = n-1
        while l<=r:
            mid = l+(r-l)//2
            if matrix[mid][0] == target:
                return True
            elif matrix[mid][0]<target:
                l = mid+1
            else:
                r = mid-1
        a = matrix[l-1]
        low = 0
        high = m-1
        while low<=high:
            mid = low + (high-low)//2
            if a[mid]==target:
                return True
            elif a[mid]<target:
                low = mid+1 
            else:
                high = mid-1
        return False       