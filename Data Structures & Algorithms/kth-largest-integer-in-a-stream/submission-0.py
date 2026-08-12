class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.l = nums[:]
        self.x = k

    def add(self, val: int) -> int:
        self.l.append(val)
        self.l.sort()
        return self.l[-self.x]

