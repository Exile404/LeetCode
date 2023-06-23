class Solution:
    def reverseVowels(self, s: str) -> str:
        l = list(s)
        v = []
        x = 'AEIOUaeiou'
        for i in l:
            if i in x:
                v.append(i)
        n = len(v)-1
        for i in range(len(l)):
            if l[i] in x:
                l[i] = v[n]
                n-=1
        return ''.join(l)
