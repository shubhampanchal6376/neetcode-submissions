
class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        length = mountainArr.length()

        # Find peak
        l, r = 0, length - 1
        while l < r:
            m = (l + r) // 2
            if mountainArr.get(m) < mountainArr.get(m + 1):
                l = m + 1
            else:
                r = m
        peak = l

        # Search left portion (ascending)
        l, r = 0, peak
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val < target:
                l = m + 1
            elif val > target:
                r = m - 1
            else:
                return m

        # Search right portion (descending)
        l, r = peak + 1, length - 1
        while l <= r:
            m = (l + r) // 2
            val = mountainArr.get(m)

            if val > target:
                l = m + 1
            elif val < target:
                r = m - 1
            else:
                return m

        return -1
