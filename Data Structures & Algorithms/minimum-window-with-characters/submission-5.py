class Solution:
    def minWindow(self, s: str, t: str) -> str:
        low = 0
        ans = float('inf')
        a = [0] * 256
        start = 0

        for i in range(len(t)):
            a[ord(t[i])] += 1

        b = [0] * 256
        required = len(t)

        def fun(ch, a, b, required):
            if b[ch] <= a[ch]:
                required -= 1
            return required

        for high in range(len(s)):
            ch = ord(s[high])
            b[ch] += 1
            required = fun(ch, a, b, required)

            while required == 0:
                l = high - low + 1

                if ans > l:
                    ans = l
                    start = low

                left = ord(s[low])

                if b[left] <= a[left]:
                    required += 1

                b[left] -= 1
                low += 1

        if ans == float('inf'):
            return ""

        return s[start:start + ans]