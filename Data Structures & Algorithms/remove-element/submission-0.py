class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        ans = []
        for i in nums:
            if i != val:
                ans.append(i)
        k = len(ans)
        nums.clear()
        for i in ans:
            nums.append(i)
        return k 