class Solution:
    def reverseWords(self, s: str) -> str:
        
        s = s.strip()
        l = s.split()
        return ' '.join(l[::-1])
