class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = [-1]
        max_length = 0
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                stack.pop()
                if stack:
                    max_length = max(max_length, i - stack[-1])
                else:
                    stack.append(i)
        return max_length

