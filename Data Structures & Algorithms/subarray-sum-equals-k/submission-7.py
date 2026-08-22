class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = defaultdict(int)
        curr = 0
        total = 0 
        for i in nums:
            prefix[curr]+=1
            curr+=i
            total += prefix[curr-k]
        return total