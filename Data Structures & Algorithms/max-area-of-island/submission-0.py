class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        maxArea = 0
        def dfs(r, c):
            if (min(r, c) < 0 or
                r == ROWS or c == COLS or
                (r,c) in visited or
                grid[r][c] == 0 
            ):
                return 0
                
            count = 1
            visited.add((r, c))
            count += dfs(r + 1, c)
            count += dfs(r - 1, c)
            count += dfs(r, c + 1)
            count += dfs(r, c - 1)

            return count

        for i in range(ROWS):
            for j in range(COLS):
                if(grid[i][j] == 1 and (i, j) not in visited):                    
                    result = dfs(i, j)
                    maxArea = max(result, maxArea)
        
        return maxArea