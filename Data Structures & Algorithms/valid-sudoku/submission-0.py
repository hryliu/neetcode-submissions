class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        board_len = 9
        rows = defaultdict(list)
        cols = defaultdict(list)
        grids = defaultdict(list)

        # grids
        # 0 1 2
        # 3 4 5
        # 6 7 8

        for i in range(board_len):
            for j in range(board_len):
                num = board[i][j]
                if num != '.':
                    rows[i].append(num)
                    cols[j].append(num)

                    grid_idx = (math.floor(i/3), math.floor(j/3))
                    grids[grid_idx].append(num)
        
        for v in rows.values():
            if len(v) != len(set(v)):
                return False

        for v in cols.values():
            if len(v) != len(set(v)):
                return False 

        for v in grids.values():
            if len(v) != len(set(v)):
                return False 

        return True