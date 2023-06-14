class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend//divisor >= (2**31)-1:
            return (2**31)-1

        elif dividend%divisor==0:
            return dividend//divisor
        elif(dividend//divisor)>=0:
            return dividend//divisor
        else:
            return (dividend//divisor)+1
