class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        a = {}
        s = "balloon"
        for i in s:
            if i == 'l' or i == 'o':
                a[i]=text.count(i)//2
            else:
                a[i]=text.count(i)
        ans = []
        for i in a.values():
            ans.append(i)
        return min(ans)
        
              