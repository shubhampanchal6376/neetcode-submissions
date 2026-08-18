class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        a = [0]*n
        for i in range(len(boxes)):
            for j in range(len(boxes)):
                if boxes[j]=="1":
                    a[i]+=abs(j-i)
        return a