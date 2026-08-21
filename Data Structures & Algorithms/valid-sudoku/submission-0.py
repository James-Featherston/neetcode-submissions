class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        default = [False] * 9
        def checkBox(i, j):
            used = default.copy()
            for row in range(3):
                for col in range(3):
                    if board[row + i][col + j] == ".":
                        continue
                    num = ord(board[row + i][col + j]) - ord("1")
                    if used[num]:
                        return False
                    used[num] = True
            return True
        def checkRow(row):
            used = default.copy()
            for col in range(9):
                if board[row][col] == ".":
                    continue
                num = ord(board[row][col]) - ord("1")
                if used[num]:
                    return False
                used[num] = True
            return True

        def checkCol(col):
            used = default.copy()
            for row in range(9):
                if board[row][col] == ".":
                    continue
                num = ord(board[row][col]) - ord("1")
                if used[num]:
                    return False
                used[num] = True
            return True


        for i in range(9):
            if not checkRow(i):
                return False
            if not checkCol(i):
                return False
        
        for i in range(0, 7, 3):
            for j in range(0, 7, 3):
                if not checkBox(i, j):
                    return False
        return True
        