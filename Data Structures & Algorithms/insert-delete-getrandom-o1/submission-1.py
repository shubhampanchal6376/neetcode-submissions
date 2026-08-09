class RandomizedSet:

    def __init__(self):
        self.m = {}
        self.l = []

    def insert(self, val: int) -> bool:
        a = val not in self.m
        if a:
            self.m[val] = len(self.l)
            self.l.append(val)
        return a

    def remove(self, val: int) -> bool:
        a = val in self.m
        if a :
            i = self.m[val]
            e = self.l[-1]
            self.l[i] = e
            self.l.pop()
            self.m[e] = i
            del self.m[val]
        return a

    def getRandom(self) -> int:
        return random.choice(self.l)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()