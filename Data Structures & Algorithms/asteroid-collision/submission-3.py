class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []
        for i in asteroids:
            if not s:
                s.append(i)
                continue
            while s and s[-1]>0 and i < 0:
                if abs(s[-1])<abs(i):
                    s.pop()
                elif abs(s[-1])==abs(i):
                    s.pop()
                    break  
                else:
                    break
            else:
                s.append(i)
        return s