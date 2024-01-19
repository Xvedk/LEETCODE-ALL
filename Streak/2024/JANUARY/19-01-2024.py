from typing import List

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        n = len(matrix)
        
        # Create a dp array to store the minimum falling path sum for each cell
        dp = [[0] * n for _ in range(n)]
        
        # Initialize the first row of dp with the same values as the first row of the matrix
        dp[0] = matrix[0]
        
        # Iterate through the matrix starting from the second row
        for i in range(1, n):
            for j in range(n):
                # Calculate the minimum falling path sum for each cell
                dp[i][j] = matrix[i][j] + min(dp[i-1][max(0, j-1):min(n, j+2)])
        
        # Return the minimum value from the last row of dp
        return min(dp[-1])


