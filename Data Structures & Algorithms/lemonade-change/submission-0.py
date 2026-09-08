class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five = 0 
        ten = 0
        for i in bills:
            if i == 5:
                five+=1
            elif i == 10:
                if five == 0:
                    return False
                five-=1
                ten+=1
            elif i == 20:
                if ten>0:
                    ten-=1
                    if five==0:
                        return False
                    five-=1
                else:
                    if five<3:
                        return False
                    five = five-3
        return True
                    