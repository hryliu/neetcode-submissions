class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        rows = len(matrix)
        cols = len(matrix[0])
        layers = [[] for _ in range(math.ceil(min(rows, cols) / 2))]

        up, down, left, right = 0, rows - 1, 0, cols - 1
        for l in layers:
            # add everything in first row
            for j in range(left, right + 1):
                l.append(matrix[up][j])

            # add everything on right side
            for i in range(up + 1, down):
                l.append(matrix[i][right])

            if up != down:
                # add bottom
                for j in range(right, left - 1, -1):
                    l.append(matrix[down][j])

            if left != right:
                # add left
                for i in range(down - 1, up, -1):
                    l.append(matrix[i][left])

            up += 1
            right -= 1
            left += 1
            down -= 1 

        print(layers)
        return [item for sublist in layers for item in sublist]
        

        
