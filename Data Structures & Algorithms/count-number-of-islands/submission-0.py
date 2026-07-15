class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        count = 0
        found = [[0 for _ in range(cols)] for _ in range(rows)]

        def bfs(r: int, c: int):
            found[r][c] = 1
            # left, right, down, up
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

            for dx, dy in dirs:
                if r + dx < 0 or r + dx >= rows or c + dy < 0 or c + dy >= cols or found[r + dx][c + dy] == 1:
                    continue
                if grid[r + dx][c + dy] == '1':
                    bfs(r + dx, c + dy)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and found[r][c] == 0:
                    bfs(r, c)
                    count += 1

        print(found)
        
        return count

        