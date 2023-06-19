class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            if s == "inf" or s == "-inf" or s=="+inf" or s=="Infinity" or s=="-Infinity" or s=="+Infinity":
                return False
            x = float(s)
            return True
        except:
            return False
