class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        f = []
        l = []
        for i in emails:
            for j in range(len(i)):
                if i[j] == "@":
                    y = i[:j]
                    x = i[j+1:]
                    f.append(i[:j])
                    l.append(i[j+1:])
                    break
        a = []
        for i in f:
            for j in range(len(i)):
                if i[j] == "+":
                    i = i[:j]
                    break
            i = i.replace(".","")
            a.append(i)
        for i in range(len(a)):
            a[i]+=l[i]
        return len(set(a))
        