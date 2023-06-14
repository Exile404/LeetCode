class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        cnt = 0
        n = len(needle)
        for i in range(len(haystack)-n+1):
            if haystack[i:i+n] == needle:
                cnt = i
                return cnt
        return -1
