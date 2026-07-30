class Bucket:
    def __init__(self):
        self.container = []
    def insert(self,val):
        if val not in self.container:
            self.container.insert(0,val)
    def remove(self,val):
        if val in self.container:
            self.container.remove(val)
    def contains(self,val):
        return val in self.container
class MyHashSet:

    def __init__(self):
        self.numBuckets = 769
        self.buckets = []
        for i in range(self.numBuckets):
            self.buckets.append(Bucket())

    def getIndex(self,key):
        return key%self.numBuckets

    def add(self, key: int) -> None:
        bucketIndex = self.getIndex(key)
        self.buckets[bucketIndex].insert(key)

    def remove(self, key: int) -> None:
        bucketIndex = self.getIndex(key)
        self.buckets[bucketIndex].remove(key)

    def contains(self, key: int) -> bool:
        bucketIndex = self.getIndex(key)
        return self.buckets[bucketIndex].contains(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)