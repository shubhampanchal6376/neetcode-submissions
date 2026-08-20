class Solution:
    def minOperations(self, logs: List[str]) -> int:
        s = []
        for i in logs:
            if i == "../" and len(s)!=0:
                s.pop()
            elif i == "../" and len(s)==0:
                continue
            elif i == "./":
                continue
            else:
                s.append(i)
        return len(s)