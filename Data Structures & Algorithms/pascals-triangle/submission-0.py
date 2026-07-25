class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1: return [[1]]

        res = [[1], [1, 1]]

        for r in range(3, numRows + 1):
            row = [1] * r
            for i in range(1, int(math.ceil(r / 2))):
                row[i] = res[r - 2][i - 1] + res[r - 2][r - 2 - i]

            for i in range(int(math.ceil(r / 2))):
                row[r - 1 - i] = row[i]

            res.append(row)

        return res
