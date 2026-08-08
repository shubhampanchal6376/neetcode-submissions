class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        x = list(set(nums))
        x.sort()
        i = 0 
        a = []
        cnt = 1 
        n = len(x)
        while i<n-1: 
            if x[i]+1 == x[i+1]:
                cnt+=1
            else:
                a.append(cnt)
                cnt = 1
            i+=1
        if len(a)==0:
            return n
        else:
            a.append(cnt)
            return max(a)