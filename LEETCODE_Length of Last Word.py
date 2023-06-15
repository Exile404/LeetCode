class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()
        l = []
        for i in s:
            l.append(i.strip())
        return len(l[len(l)-1])
