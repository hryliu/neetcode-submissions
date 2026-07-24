class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        visited = set()

        def dfs(row, col, idx):
            if idx == len(word):
                return True

            dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for dr, dc in dirs:
                nr, nc = row + dr, col + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if board[nr][nc] == word[idx] and (nr, nc) not in visited:
                        visited.add((nr, nc))
                        if dfs(nr, nc, idx + 1): return True
                        visited.remove((nr, nc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    if dfs(i, j, 1): return True
                    visited.remove((i, j))

        return False

        