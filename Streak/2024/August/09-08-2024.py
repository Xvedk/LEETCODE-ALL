from typing import List

class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        def check_equal_row_sums(matrix):
            # Calculate the sum of the first row
            row_sum = sum(matrix[0])
            # Check if all other rows have the same sum
            for row in matrix:
                if sum(row) != row_sum:
                    return False
            return True
        
        def check_equal_col_sum(matrix):
            # Transpose the matrix to check column sums using row sum checker
            transposed = [list(row) for row in zip(*matrix)]
            return check_equal_row_sums(transposed)
        
        def check_diagonals(matrix):
            n = len(matrix)
            # Sum of the main diagonal (top-left to bottom-right)
            d1 = sum(matrix[i][i] for i in range(n))
            # Sum of the anti-diagonal (top-right to bottom-left)
            d2 = sum(matrix[i][n-i-1] for i in range(n))
            # Both diagonals must have the same sum and match the row sum
            return d1 == d2 and d1 == sum(matrix[0])
        
        def is_magic_square(matrix):
            # Flatten the matrix and sort to check for all numbers 1-9
            flattened = [num for row in matrix for num in row]
            if sorted(flattened) != list(range(1, 10)):
                return False
            # Check row sums, column sums, and diagonal sums
            return check_equal_row_sums(matrix) and check_equal_col_sum(matrix) and check_diagonals(matrix)
        
        count = 0
        rows, cols = len(grid), len(grid[0])
        
        # Loop through each possible 3x3 subgrid
        for i in range(rows - 2):
            for j in range(cols - 2):
                subgrid = [row[j:j+3] for row in grid[i:i+3]]
                if is_magic_square(subgrid):
                    count += 1
        
        return count
