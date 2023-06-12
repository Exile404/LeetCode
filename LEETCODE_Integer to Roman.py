class Solution:
    def intToRoman(self, num: int) -> str:
        num_arr = [1, 4, 5, 9, 10, 40, 50, 90,100, 400, 500, 900, 1000]
        sym_arr = ["I", "IV", "V", "IX", "X", "XL","L", "XC", "C", "CD", "D", "CM", "M"]
        i = 12
        s= ''
        while num:
            div = num // num_arr[i]
            num %= num_arr[i]

            while div:
                s+=sym_arr[i]
                div -= 1
            i -= 1
        return s
