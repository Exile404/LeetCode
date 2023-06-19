class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
    
        
        dp[0][0] = True
        len_p = len(p)
        len_s = len(s)
        
        for j in range(1, len_p + 1):
            if p[j - 1] == '*':
                dp[0][j] = dp[0][j - 1]
        
        for i in range(1, len_s + 1):
            for j in range(1, len_p + 1):
                if p[j - 1] == '?' or s[i - 1] == p[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                elif p[j - 1] == '*':
                    dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
        
        return dp[-1][-1]
