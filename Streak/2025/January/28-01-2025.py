class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def collect_fish(i, j):
            num_fish = grid[i][j] # collect fish from current cell
            grid[i][j] = 0 # caught fish in current cell, no more remaining

            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]: # explore adjacent cells
                ni, nj = i + di, j + dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] != 0: 
                    num_fish += collect_fish(ni, nj) # if cell in bounds and has fish, collect

            return num_fish

        m = len(grid)
        n = len(grid[0])
        max_fish = 0
        for i in range(m): # loop through each cell and update max fish if cell's section has more
            for j in range(n):
                if grid[i][j] == 0: continue
                max_fish = max(max_fish, collect_fish(i, j))

        return max_fish
