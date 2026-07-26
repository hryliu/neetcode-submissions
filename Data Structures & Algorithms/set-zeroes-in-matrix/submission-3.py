class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        first_row_zero = any(matrix[0][c] == 0 for c in range(cols))
        first_col_zero = any(matrix[r][0] == 0 for r in range(rows))

        def rows_helper(r):
            for col in range(cols):
                matrix[r][col] = 0

        def cols_helper(c):
            for row in range(rows):
                matrix[row][c] = 0

        # mark using only the interior (skip row 0 / col 0 themselves)
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    matrix[r][0] = 0

        for c in range(1, cols):
            if matrix[0][c] == 0:
                cols_helper(c)

        for r in range(1, rows):
            if matrix[r][0] == 0:
                rows_helper(r)

        if first_row_zero:
            rows_helper(0)
        if first_col_zero:
            cols_helper(0)