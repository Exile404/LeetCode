class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        subs = []
        sz = 0
        start = 0
        end = 0
        size = len(s)
        while end<size:
            if s[end] not in subs:
                subs.append(s[end])
                end+=1
                sz = max(sz,end-start)
            else:
                subs.remove(s[start])
                start+=1
        return sz
