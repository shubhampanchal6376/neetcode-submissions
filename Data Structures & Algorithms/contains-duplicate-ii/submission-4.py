class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        m = {}
        for i in range(len(nums)):
            if nums[i] in m:
                if i - m[nums[i]] <=k :
                    return True
                else:
                    m[nums[i]] = i
            else:
                m[nums[i]] = i
        return False