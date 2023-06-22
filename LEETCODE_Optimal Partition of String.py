class Solution:
    def partitionString(self, s: str) -> int:
        s1 = ''
        count = 0
        l = []
        for i in range(len(s)):
            if s[i] not in s1:
                s1+=s[i]
            elif s[i] in s1:
                count+=1
                s1 = s[i]
        return count+1
