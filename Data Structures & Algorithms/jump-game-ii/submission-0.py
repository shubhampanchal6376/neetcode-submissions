class Solution:
    def jump(self, nums: list[int]) -> int:
        if len(nums)<=1:
            return 0
        n = len(nums)
        jumps = 0 
        curr_reach = 0
        farthest = 0 
        for i in range(n-1):
            farthest  = max(farthest,i+nums[i])
            if i == curr_reach:
                jumps+=1
                curr_reach = farthest 
                if curr_reach>=n-1:
                    return jumps
        return -1