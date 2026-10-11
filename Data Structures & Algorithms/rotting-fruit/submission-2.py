class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        fresh = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue and fresh > 0:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dirX, dirY in directions:
                    newX, newY = x + dirX, y + dirY
                    if 0 <= newX < rows and 0 <= newY < cols and grid[newX][newY] == 1:
                        grid[newX][newY] = 2
                        fresh -= 1
                        queue.append((newX, newY))
            minutes += 1

        return minutes if fresh == 0 else -1