class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        shift = min(nums)
        m = max(nums)
        if shift == m:
            return nums
        m = m-shift
        # let no. of buckets = 5
        k = 5
        n = len(nums)
        # creating k number of buckets 
        b = [[] for i in range(k)]
        # filling the elements in the buckets 
        for i in nums:
            # finding the index of the bucket to store that element into it 
            idx = (i-shift)*k//m
            # if index of bucket is equal to the k then put it into the previous bucket means the last bucket 
            if idx == k:
                idx = k-1
            b[idx].append(i)
        # sorting the buckets 
        for i in b:
            i.sort()
        ans = []
        # concatenating the buckets
        for i in range(len(b)):
            for j in b[i]:
                ans.append(j)
        return ans

        
           