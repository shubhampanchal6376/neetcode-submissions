class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return pow(num,0.5).is_integer()