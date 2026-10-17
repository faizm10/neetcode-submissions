class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        maxArea = 0
        directions = [
            (1,0),(-1,0),(0,1),(0,-1)
        ]
        def dfs(r,c):
        
            if grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            count=1
            for dr,dc in directions:
                newRow=dr+r
                newCol=dc+c
                # check to see if it is inside the boundary
                if 0<=newRow<rows and 0<=newCol<cols:
                    if grid[newRow][newCol] == 1:
                        count+=dfs(newRow,newCol)
                else:
                    continue
            return count
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == 1:
                    count = 0
                    maxArea = max(dfs(row,col),maxArea)
        return maxArea