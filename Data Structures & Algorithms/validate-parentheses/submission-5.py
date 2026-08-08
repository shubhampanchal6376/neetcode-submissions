class Solution:
    def isValid(self, s: str) -> bool:
        a = []
        if s[0] == "]" or s[0] == "}" or s[0] == ")":
            return False
        for i in s:
            if i == "[" or i == "{" or i == "(":
                a.append(i)
            elif i == "]":
                if len(a)!=0 and a[-1] == "[" :
                    a.pop()
                else:
                    return False
            elif i == "}":
                if len(a)!=0 and a[-1] == "{":
                    a.pop()
                else:
                    return False
            elif i == ")":
                if len(a)!=0 and a[-1] == "(":
                    a.pop()
                else:
                    return False
            else:
                return False
        return len(a)==0