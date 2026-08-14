class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        for i in tokens:
            if i == "+" :
                a = s.pop()
                b = s.pop()
                c = int(a)+int(b)
                s.append(c)
            elif i == "-" :
                a = s.pop()
                b = s.pop()
                c = int(b)-int(a)
                s.append(c)
            elif i == "*" :
                a = s.pop()
                b = s.pop()
                c = int(a)*int(b)
                s.append(c)
            elif i == "/" :
                a = s.pop()
                b = s.pop()
                y = False
                if (a<0 and b>0) or (a>0 and b<0 ):
                    y = True
                    a = -a
                c = int(b)//int(a)
                if y:
                    s.append(-c)
                else:
                    s.append(c)
            else:
                s.append(int(i))
        return sum(s)