class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid
        m = len(grid)
        n = len(grid[0])
        
        # Initialize the maximum operations to zero
        maxOp = 0
        
        # Create a DP table initialized to zero
        dp = [[0] * n for _ in range(m)]
        
        # Directions array to explore neighboring rows (up, same, down)
        direction = [-1, 0, 1]
        
        # Iterate over each column
        for j in range(n):
            # Iterate over each row
            for i in range(m):
                # Check if current cell in dp table equals to the column index
                if dp[i][j] == j:
                    # Explore all three possible row movements
                    for ni in direction:
                        # Check boundaries and conditions to update dp table
                        if 0 <= i + ni < m and 0 < j + 1 < n and grid[i + ni][j + 1] > grid[i][j] and dp[i][j] + 1 > dp[i + ni][j + 1]:
                            # Update the dp table with the new maximum moves
                            dp[i + ni][j + 1] = dp[i][j] + 1
                            # Update the maxOp if the new value is greater
                            if dp[i + ni][j + 1] > maxOp:
                                maxOp = dp[i + ni][j + 1]
                                # If maxOp reaches the last column, return it immediately
                                if maxOp == n - 1:
                                    return maxOp
        # Return the maximum operations found
        return maxOp
