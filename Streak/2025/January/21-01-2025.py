class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        row, col = sum(grid[0][1:]), 0
        res = row
        for i in range(1, len(grid[0])):
            row -= grid[0][i]
            col += grid[1][i - 1]

            if res >= max(row, col):
                res = max(row, col)
            else:
                return res
        
        return res
