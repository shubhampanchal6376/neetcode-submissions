class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        l = 0
        r = k
        n =len(arr)
        cnt = 0 
        s = sum(arr[l:r])
        while r<=n:
            if s//k>=threshold:
                cnt+=1
            if r>=n:
                break
            s = s - arr[l] + arr[r]
            l+=1
            r+=1                                                         
        return cnt