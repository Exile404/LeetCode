class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip()  # Remove leading and trailing whitespace
        if not s:
            return 0  # Empty string

        sign = 1
        if s[0] == '-':
            sign = -1
            s = s[1:]
        elif s[0] == '+':
            s = s[1:]

        num = 0
        for char in s:
            if not char.isdigit():
                break
            num = num * 10 + int(char)

        num = sign * num
        num = max(-2**31, min(num, 2**31 - 1))  # Clamp the integer to the specified range
        return num
