class Solution:
    def helper(self,s:str,n:int,idx:int,m:dict,diary:list[str],ans:list[str]):
        if idx==n:
            ans.append("".join(diary))
            return 
        choices = m[s[idx]]
        for i in choices:
            diary.append(i)
            self.helper(s,n,idx+1,m,diary,ans)
            diary.pop()
        return 
    def letterCombinations(self, digits: str) -> List[str]:
        if digits=="":
            return list(digits)
        m ={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        n = len(digits)
        diary = []
        ans = []
        self.helper(digits,n,0,m,diary,ans)
        return ans