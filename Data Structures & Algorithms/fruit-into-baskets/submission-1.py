class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        ans = 0 
        low = 0
        m = {}
        for high in range(len(fruits)):
            m[fruits[high]] = m.get(fruits[high],0)+1
            while len(m)>2:
                m[fruits[low]]-=1
                if m[fruits[low]]==0:
                    del m[fruits[low]]
                low+=1
            if len(m)<=2:
                ans = max(ans,high-low+1)
        return ans 
