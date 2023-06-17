class Solution:
    def addBinary(self, a: str, b: str) -> str:
        bin_sum = int(a,2) + int(b,2)
        bin_ans = bin(bin_sum)[2:]
        return bin_ans
