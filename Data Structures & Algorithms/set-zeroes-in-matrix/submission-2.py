class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        zero_rows = set()
        zero_cols = set()

        def rows_helper(r):
            # set row to 0
            for col in range(cols):
                matrix[r][col] = 0

        def cols_helper(c):
            # set col to 0
            for row in range(rows):
                matrix[row][c] = 0

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in zero_rows:
            rows_helper(r)

        for c in zero_cols:
            cols_helper(c)
        