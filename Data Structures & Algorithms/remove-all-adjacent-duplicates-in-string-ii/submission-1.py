class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        st = []
        for i in s:
            st.append(i)
            if len(st)>=k:
                if len(set(st[-k:]))==1:
                    st = st[:-k]
        return "".join(st)