class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        for x in range(1,m):
            grid[x][0] += grid[x-1][0] 
        for x in range(1,n):
            grid[0][x] += grid[0][x-1]
        
        for i in range(1,m):
            for j in range(1,n):
                grid[i][j]+=min(grid[i][j-1],grid[i-1][j])
        return grid[m-1][n-1]
