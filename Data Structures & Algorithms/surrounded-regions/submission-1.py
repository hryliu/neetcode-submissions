class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])

        # visited = set()
        
        # queue = deque()
        # surrounded = defaultdict(dict)

        # def bfs(queue):
        #     dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        #     while(queue):
        #         x, y = queue.popleft()
        #         print(x, y)

        #         for dx, dy in dirs:
        #             if x + dx not in range(rows) or y + dy not in range(cols):
        #                 print("not in range: ", x + dx, y + dy)
        #                 surrounded[(x, y)][(dx, dy)] = False

        #             if x + dx in range(rows) and y + dy in range(cols):
        #                 if board[x + dx][y + dy] == 'X':
        #                     surrounded[(x, y)][(dx, dy)] = True

        #                 if board[x + dx][y + dy] == 'O':
        #                     surrounded_items = list(surrounded[(x, y)].values())
        #                     if None not in surrounded_items and False not in surrounded_items:
        #                         board[x][y] = 'X'

        #                     if None in surrounded_items:
        #                         queue.append((x + dx, y + dy))  

        def dfs(x, y, visited):
             if (x == 0 or x + 1 == rows or y == 0 or y + 1 == cols) and board[x][y] == 'O':
                # visited.add((x + dx, y + dy))
                return False

             dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

             for dx, dy in dirs:
                if x + dx in range(rows) and y + dy in range(cols) and board[x + dx][y + dy] == 'O':
                    if (x + dx, y + dy) not in visited:
                        visited.add((x + dx, y + dy))
                        dfs(x + dx, y + dy, visited)

             for vx, vy in visited:
                if (vx == 0 or vx + 1 == rows or vy == 0 or vy + 1 == cols) and board[vx][vy] == 'O':
                    return False

             return True
                        
        for x in range(rows): 
            for y in range(cols):
                if board[x][y] == 'O':
                    if dfs(x, y, set()):
                        board[x][y] = 'X'