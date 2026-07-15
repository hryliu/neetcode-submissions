class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            print("x, y: ", r, ", ", c)
            area = 1
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in dirs:
                if r + dx in range(rows) and c + dy in range(cols) and grid[r + dx][c + dy] == 1:
                    grid[r + dx][c + dy] = 0
                    area += dfs(r + dx, c + dy)

            return area

        for r in range(rows):
            for c in range(cols):
                # island found
                if grid[r][c] == 1:
                    grid[r][c] = 0
                    area = dfs(r, c)

                    max_area = max(area, max_area)

                    print("area: ", area)

        return max_area


        