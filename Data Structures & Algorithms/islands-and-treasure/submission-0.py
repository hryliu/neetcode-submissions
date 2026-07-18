class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid) 
        cols = len(grid[0])

        def bfs(queue):
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            while queue:
                for _ in range(len(queue)):
                    x, y, distance = queue.popleft()
                    for dx, dy in dirs:
                        if x + dx in range(rows) and y + dy in range(cols) and grid[x + dx][y + dy] > 0:
                            curr_distance = distance + 1
                            min_distance = min(grid[x + dx][y + dy], curr_distance)

                            if min_distance != grid[x + dx][y + dy]:
                                grid[x + dx][y + dy] = min_distance
                                queue.append((x + dx, y + dy, min_distance))

        queue = deque()

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 0:
                    queue.append((x, y, 0))

        bfs(queue)