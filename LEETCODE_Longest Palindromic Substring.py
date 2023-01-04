class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        def check(s,l,r):
            while l>=0 and r< len(s) and s[r] == s[l]:
                l-=1
                r+=1
            return s[l+1:r]
        lp = ''
        for i in range(len(s)):
            pal = check(s,i,i)
            if len(pal)>len(lp):
                lp = pal
            pal = check(s,i,i+1)
            if len(pal)>len(lp):
                lp = pal
        return lp
