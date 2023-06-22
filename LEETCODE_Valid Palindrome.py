class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s1 = ''
        for i in s:
            if 'a'<=i<='z' or '0'<=i<='9':
                s1+=i
        if s1 == s1[::-1]:
            return True
        return False
