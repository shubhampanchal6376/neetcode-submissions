class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        a = s.count("1")
        b = s.count("0")
        x = ""
        if a>1:
            for i in range(a-1):
                x+="1"
            for i in range(b):
                x+="0"
            x+="1"
        else:
            for i in range(b):
                x+="0"
            x+="1"
        return x