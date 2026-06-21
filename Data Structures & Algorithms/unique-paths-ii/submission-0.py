class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        columns = len(obstacleGrid[0])

        prevRow = [0] * columns
        prevRow[columns - 1] = 1

        for i in range(rows - 1, -1, -1):
            curRow = [0] * columns
            for j in range(columns - 1, -1, -1):
                pathSum = curRow [j + 1] + prevRow[j] if j < columns - 1 else prevRow[j]
                curRow[j] = 0 if obstacleGrid[i][j] == 1 else pathSum
            
            prevRow = curRow

        return prevRow[0]