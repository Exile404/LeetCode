class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ''
        for i in digits:
            s+=str(i)
        l = str(int(s)+1)
        num = [int(i) for i in l]
        return num
