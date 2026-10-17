class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        directions = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ] 
        def dfs(r,c):
            if grid[r][c] == '0':
                return
            grid[r][c] = '0'
            for dr,dc in directions:
                newRow = dr + r
                newCol = dc + c
                if 0<=newRow<rows and 0<=newCol<cols:
                    if grid[newRow][newCol] == '1':
                        dfs(newRow,newCol)
                else:
                    continue
                    
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row,col)
                    count+=1
        return count