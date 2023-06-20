class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s
        result=[""] * numRows
        idx, st = 0,1
        for i in s:
            result[idx] += i
            if idx == 0:
                st = 1
            elif idx == numRows-1:
                st = -1
            idx+=st
        return ''.join(result)
