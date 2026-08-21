class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count = 0
        x, y = 0, 0
        found = False
        curr = []
        for i in range(len(grid)):
            for j in range (len(grid[0])):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    found = True
                    curr.append([i, j])
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        if count == 0:
            return 0
        if not found:
            return -1
        nxt = []
        timer = 0
        while count != 0 and len(curr) > 0:
            timer += 1
            for elem in curr:
                if self.check(elem[0] + 1, elem[1], visited, grid):
                    nxt.append([elem[0] + 1, elem[1]])
                    count -= 1
                if self.check(elem[0] - 1, elem[1], visited, grid):
                    nxt.append([elem[0] - 1, elem[1]])
                    count -= 1
                if self.check(elem[0], elem[1] + 1, visited, grid):
                    count -= 1
                    nxt.append([elem[0], elem[1] + 1])
                if self.check(elem[0], elem[1] - 1, visited, grid):
                    count -= 1
                    nxt.append([elem[0], elem[1] - 1])
            curr = nxt
            nxt = []
        if count != 0:
            return -1
        return timer
    def check(self, x, y, visited, grid):
        if x < 0 or x >= len(visited) or y < 0 or y >= len(visited[0]):
            return False
        if visited[x][y]:
            return False
        visited[x][y] = True
        if grid[x][y] == 1:
            return True
        return False

            


        