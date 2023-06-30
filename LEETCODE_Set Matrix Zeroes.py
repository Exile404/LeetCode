class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows, cols = len(matrix), len(matrix[0])
        sentinel = float('-inf')

        # Mark rows and columns to be set to zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    # Use sentinel value to mark the rows and columns to avoid conflicts
                    for k in range(rows):
                        if matrix[k][j] != 0:
                            matrix[k][j] = sentinel
                    for k in range(cols):
                        if matrix[i][k] != 0:
                            matrix[i][k] = sentinel

        # Set marked rows and columns to zero
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == sentinel:
                    matrix[i][j] = 0
