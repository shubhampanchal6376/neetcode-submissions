class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        sum = 0 
        for i in words:
            x = 0 
            for j in i:
                if i.count(j)>chars.count(j):
                    x = 1
            if x == 0:
                sum += len(i)
        return sum
