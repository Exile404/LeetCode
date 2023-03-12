class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        x = []
        for i in range(n):
            l = []
            for j in range(n-1,-1,-1):
                l.append(matrix[j][i])
            matrix.append(l)

        for i in range(n):
            matrix.pop(0)
        
