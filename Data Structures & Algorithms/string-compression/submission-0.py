class Solution:
    def compress(self, chars: List[str]) -> int:
        s = ""
        n = 1
        t = len(chars)
        if t == 1:
            return 1
        for i in range(len(chars)-1):
            if chars[i]==chars[i+1]:
                n+=1
            else:
                if n>1:
                    s+=(chars[i]+str(n))
                else:
                    s+=chars[i]
                n=1
        if chars[-1]!=chars[-2]:
            s+=chars[-1]
        else:
            s+=chars[-1]
            s+=str(n)
        chars[:len(s)] = list(s)
        return len(s)