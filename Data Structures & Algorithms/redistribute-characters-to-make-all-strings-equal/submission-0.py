class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        a = ""
        n = len(words) 
        for i in words:
            a += i
        for i in set(a):
            if a.count(i)%n!= 0:
                return False
        return True
        
                   
