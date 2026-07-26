class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        def helper(r, c):
            # set row to 0
            for col in range(cols):
                if col == c:
                    continue
                matrix[r][col] = 0

            # set col to 0
            for row in range(rows):
                if row == r:
                    continue
                matrix[row][c] = 0

        zeroes = []
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeroes.append([r, c])

        for r, c in zeroes:
            helper(r, c)
        