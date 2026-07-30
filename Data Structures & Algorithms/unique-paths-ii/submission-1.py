class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 0 0 0 
        # 0 0 0
        # 0 1 0

        # paths
        # 1 1 1
        # 1 2 3
        # 1 0 3

        # if obstacle at origin, return 0

        # set row 0 (idx 1 up to row_size) to 1 (unless there is obstacle then stop)
        # set col 0 (idx 1 up to row_size) to 1 (unless obstacle)

        # loop through row and cols in grid starting from idx 1 for row and col
        # if no obstacle, set paths[i][j] to paths[i - 1][j] + paths[i][j - 1]
        
        # return paths[rows - 1][cols - 1]

        # time = space = o(num rows * nums cols)

        if obstacleGrid[0][0] == 1: return 0

        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])

        paths = [[0] * cols for _ in range(rows)]

        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                break
            paths[i][0] = 1

        for j in range(cols):
            if obstacleGrid[0][j] == 1:
                break
            paths[0][j] = 1

        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i - 1][j] + paths[i][j - 1]

        return paths[rows - 1][cols - 1]



