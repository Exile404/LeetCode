class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a
        len1, len2 = len(str1), len(str2)
        divisor_len = gcd(len1, len2)
        divisor = str1[:divisor_len]
        if divisor * (len1 // divisor_len) == str1 and divisor * (len2 // divisor_len) == str2:
            return divisor
        else:
            return ""
