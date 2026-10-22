class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0]*n
        res[n-1]=0
        st = []
        st.append(n-1)
        for i in range(n-2,-1,-1):
            while len(st)!=0 and temperatures[st[-1]]<=temperatures[i]:
                st.pop()
            if len(st)==0:
                res[i]=0
            else:
                res[i] = st[-1]-i
            st.append(i)        
        return res