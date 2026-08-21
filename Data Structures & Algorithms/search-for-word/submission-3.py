class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        ROWS, COLS = len(board), len(board[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = [[False for _ in range(COLS)] for _ in range(ROWS)]
        def dfs(row, col, idx):
            if row < 0 or row >= ROWS or col < 0 or col >= COLS or visited[row][col]:
                return False
            visited[row][col] = True
            if word[idx] == board[row][col]:
                if idx == len(word) - 1:
                    visited[row][col] = False
                    return True
                for d in directions:
                    if dfs(row + d[0], col + d[1], idx + 1):
                        visited[row][col] = False
                        return True
            visited[row][col] = False
            return False

        start = word[0]
        for row in range(ROWS):
            for col in range(COLS):
                works = dfs(row, col, 0)
                if works:
                    return True
        return False


        