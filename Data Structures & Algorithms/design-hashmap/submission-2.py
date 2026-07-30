class Pair:
    def __init__(self, f, s):
        self.first = f
        self.second = s


class Bucket:
    def __init__(self):
        self.list = []

    def put(self, key, value):
        for p in self.list:
            if p.first == key:
                p.second = value
                return
        self.list.insert(0, Pair(key, value))

    def get(self, key):
        for p in self.list:
            if p.first == key:
                return p.second
        return -1

    def remove(self, key):
        for p in self.list:
            if p.first == key:
                self.list.remove(p)
                return


class MyHashMap:

    def __init__(self):
        self.keyRange = 769
        self.buckets = []

        for i in range(self.keyRange):
            self.buckets.append(Bucket())

    def getBucketIndex(self, key):
        return key % self.keyRange

    def put(self, key, value):
        bucketidx = self.getBucketIndex(key)
        self.buckets[bucketidx].put(key, value)

    def get(self, key):
        bucketidx = self.getBucketIndex(key)
        return self.buckets[bucketidx].get(key)

    def remove(self, key):
        bucketidx = self.getBucketIndex(key)
        self.buckets[bucketidx].remove(key)