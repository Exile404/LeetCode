import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        p = '^'+ p + '$'
        pattern = re.compile(p)
        match = re.match(pattern,s)
        if match:
            return True
        return False
