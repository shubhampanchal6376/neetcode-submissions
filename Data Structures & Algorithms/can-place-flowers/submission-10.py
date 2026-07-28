class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if n == 0 :
            return True 
        a = len(flowerbed)
        if len(flowerbed) == 1 and flowerbed[0]==0 and n==1:
            return True 
        for i in range(1, a-1):  
            if flowerbed[0] == 0 and flowerbed[1] == 0:
                n-=1
                flowerbed[0] = 1
            elif flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0 :
                n-=1
                flowerbed[i] = 1
            elif flowerbed[a-1] == 0 and flowerbed[a-2]==0:
                n-=1
                flowerbed[a-1] = 1
            else:
                if n==0: 
                    return True 
        return n <= 0 
            