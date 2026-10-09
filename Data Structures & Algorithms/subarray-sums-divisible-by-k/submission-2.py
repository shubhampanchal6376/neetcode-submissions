class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        n = len(nums)
        m = {}
        m[0] = 1
        ans = 0 
        sum =0 
        for i in range(n):
            sum+=nums[i]
            rem = sum%k
            if rem<0:
                rem = rem+k
            ans += m.get(rem,0)
            m[rem] = m.get(rem,0)+1
        return ans