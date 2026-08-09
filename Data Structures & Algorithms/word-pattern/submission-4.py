class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        t = s.split()
        m = {}
        n = len(pattern)
        x = len(t)
        if n!=x:
            return False
        for i in range(n):
            if pattern[i] not in m :
                if t[i] not in m.values():
                    m[pattern[i]] = t[i]
                else:
                    return False
            elif pattern[i] in m:
                if m[pattern[i]] == t[i]:
                    continue
                else:
                    return False
        return True
