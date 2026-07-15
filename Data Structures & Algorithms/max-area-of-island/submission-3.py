class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def dfs(r: int, c: int) -> int:
            grid[r][c] = 0
            area = 1
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in dirs:
                if r + dx in range(rows) and c + dy in range(cols) and grid[r + dx][c + dy] == 1:
                    area += dfs(r + dx, c + dy)

            return area

        def bfs(r: int, c: int) -> int:
            grid[r][c] = 0
            area = 1
            queue = deque([(r, c)])
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            while queue:
                cr, cc = queue.popleft()

                for dr, dc in dirs:
                    if cr + dr in range(rows) and cc + dc in range(cols) and grid[cr + dr][cc + dc] == 1:
                        grid[cr + dr][cc + dc] = 0
                        queue.append((cr + dr, cc + dc))
                        area += 1

            return area

        for r in range(rows):
            for c in range(cols):
                # island found
                if grid[r][c] == 1:
                    area = bfs(r, c)
                    max_area = max(area, max_area)

        return max_area


        