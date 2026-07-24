class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # iterate through each row and col
        # if value == word[0]
        # dfs
        rows = len(board)
        cols = len(board[0])

        if len(word) > rows * cols:
            return False

        res = False
        visited = set()

        def dfs(row, col, idx, visited):
            nonlocal res
            # base case: last letter matches
            if idx == len(word):
                res = True
                return

            dirs = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for dr, dc in dirs:
                if 0 <= row + dr < rows and 0 <= col + dc < cols:
                    if board[row + dr][col + dc] == word[idx] and (row + dr, col + dc) not in visited:
                        visited.add((row + dr, col + dc))
                        dfs(row + dr, col + dc, idx + 1, visited)
                        visited.remove((row + dr, col + dc))

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    visited.add((i, j))
                    dfs(i, j, 1, visited)
                    if res:
                        return True

                    visited.remove((i, j))

        return False

        