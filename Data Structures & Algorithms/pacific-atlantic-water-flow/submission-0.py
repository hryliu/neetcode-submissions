class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def get_can_visit(start_row: int, start_col: int) -> set():
            res = set()
            visited = set()

            dirs = [(0, -1), (0, 1), (-1, 0), (1, 0)]

            queue = deque([(start_row, start_col)])
            visited.add((start_row, start_col))
            res.add((start_row, start_col))

            for i in range(rows):
                queue.append((i, start_col))
                visited.add((i, start_col))
                res.add((i, start_col))

            for j in range(cols):
                queue.append((start_row, j))
                visited.add((start_row, j))
                res.add((start_row, j))

            while queue:
                r, c = queue.popleft()

                for dr, dc in dirs:
                    nr, nc = r + dr, c + dc

                    if (nr in range(rows) and nc in range(cols) 
                        and (nr, nc) not in visited 
                        and heights[r][c] <= heights[nr][nc]):
                        # new node in range and water can flow there
                        visited.add((nr, nc))
                        queue.append((nr, nc))
                        res.add((nr, nc))

            return res

        can_visit_atlantic = get_can_visit(0, 0)
        can_visit_pacific = get_can_visit(rows - 1, cols - 1)

        print(can_visit_atlantic)
        print(can_visit_pacific)
        

        return list(can_visit_atlantic & can_visit_pacific)



