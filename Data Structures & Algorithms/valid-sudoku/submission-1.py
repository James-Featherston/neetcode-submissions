class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        DIM = 9
        def getVal(s: str):
            if s == ".":
                return 0
            return ord(s) - ord("0")
        def invalidArr(arr: List(int)):
            for i in range(1, DIM + 1):
                if arr[i] > 1:
                    return True
            return False

        # Check all rows and cols
        for x in range(DIM):
            row = [0] * (DIM + 1)
            col = [0] * (DIM + 1)
            for y in range(DIM):
                row[getVal(board[x][y])] += 1
                col[getVal(board[y][x])] += 1
            if invalidArr(col) or invalidArr(row):
                return False

        # Check all boxes
        for x in range(0, DIM, 3):
            for y in range(0, DIM, 3):
                box = [0] * (DIM + 1)
                for i in range(3):
                    for j in range(3):
                        box[getVal(board[x+i][y+j])] += 1
                if invalidArr(box):
                    return False

        return True









