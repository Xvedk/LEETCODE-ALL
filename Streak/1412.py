class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:

        rows, cols = len(grid), len(grid[0])

        # Step 1: Initialize diff matrix. 
        # All updates will be made directly to this matrix.
        diff = [["" for _ in range(cols)] for _ in range(rows)]

        # Step 2: Calculate rowOneCount and rowZeroCount for each row.
        # We update (rowOneCount - rowZeroCount) directly into diff array.
        for r in range(rows):
            rowOneCount = sum(grid[r])
            rowZeroCount = cols - rowOneCount
            diff[r] = [(rowOneCount - rowZeroCount)] * cols

        # Step 3: Calculate colOneCount and colZeroCount for each column.
        # After deriving these values, we update each cell with them.
        for c in range(cols):
            colOneCount = 0
            for r in range(rows):
                colOneCount += grid[r][c]
            colZeroCount = rows - colOneCount

            # Iterate over all rows again to update every cell.
            for r in range(rows):
                diff[r][c] += (colOneCount - colZeroCount)

        return diff
