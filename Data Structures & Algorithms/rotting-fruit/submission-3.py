class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        time = 0
        queue = deque()

        def bfs(queue):
            nonlocal time
            dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
            
            while(queue):
                for _ in range(len(queue)):
                    x, y, time = queue.popleft()

                    for dx, dy in dirs:
                        if x + dx in range(rows) and y + dy in range(cols) and grid[x + dx][y + dy] == 1:
                            grid[x + dx][y + dy] = 2
                            queue.append((x + dx, y + dy, time + 1))
                

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 2:
                    queue.append((x, y, time))
        
        bfs(queue)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] == 1:
                    time = -1

        return time