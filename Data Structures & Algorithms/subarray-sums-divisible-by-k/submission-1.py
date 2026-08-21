class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        l = 0
        r = 0
        cnt = 0
        sum = 0 
        n = len(nums)
        while r < n:
            r+=1 
            sum+=nums[r-1]
            if sum % k == 0 :
                cnt+=1
            if r==n:
                l+=1
                r = l
                sum = 0 
        return cnt