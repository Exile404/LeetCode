class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # Initialize an empty chessboard
        board = [['.' for _ in range(n)] for _ in range(n)]
        solutions = []
        
        def is_safe(row,col):
            for i in range(row):
                # Check up and down for queen
                if board[i][col] == 'Q':
                    return False
            i,j = row,col
            #check upper left diagonal
            while i>=0 and j>=0:
                if board[i][j]=='Q':
                    return False
                i-=1
                j-=1
            i,j = row,col
            #check upper right diagonal
            while i>=0 and j<n:
                if board[i][j]=='Q':
                    return False
                i-=1
                j+=1
            return True
        def backtrack(row):
            if row == n:
                solutions.append([''.join(row) for row in board])
                return
            for col in range(n):
                if is_safe(row,col):
                    board[row][col] = 'Q'
                    backtrack(row+1)
                    board[row][col]= '.'
        backtrack(0)
        return solutions
    
