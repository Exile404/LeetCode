class Solution:
    def reverse(self, num: int) -> int:
        
        string = str(num)

    # reversing the string
        string = list(string)
        string.reverse()
        string = ''.join(string)

        # converting string to integer
        #num = int(string)
        n=len(string)
        if string[n-1]=='-':
            string='-'+string[:n-1]
        # returning integer
        n=int(string)
        if -2**31<n<2**31:

            return int(string)
        return 0
