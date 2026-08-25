class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k
        n =len(arr)
        cnt = 0 
        while r<=n:
            s = sum(arr[l:r])
            if s//k>=threshold:
                cnt+=1
            l+=1
            r+=1
        return cnt