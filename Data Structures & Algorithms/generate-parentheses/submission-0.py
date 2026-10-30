class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        temp = []
        def fun(open,close):
            if open==n and close==n:
                res.append("".join(temp))
                return 
            if open < n:
                temp.append('(')
                fun(open+1,close)
                temp.pop()
            if close<open:
                temp.append(')')
                fun(open,close+1)
                temp.pop()
        fun(0,0)
        return res