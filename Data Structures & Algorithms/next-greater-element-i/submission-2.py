class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        b = 0
        for i in nums1:
            for j in range(len(nums2)):
                if i == nums2[j] :
                    for k in range(j+1,len(nums2)):
                        if nums2[k] > i:
                            ans.append(nums2[k])
                            b+=1
                            break
                    ans.append(-1)
        while b>0:
            for i in range(len(ans)-1,-1,-1):
                if ans[i] == -1:
                    ans = ans[:i] + ans[i+1:]
                    break
            b-=1
        return ans