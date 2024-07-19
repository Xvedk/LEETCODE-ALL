class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        min_in_rows = {min(row) for row in matrix}  # Set of minimums from each row
        max_in_columns = {max(column) for column in zip(*matrix)}  # Set of maximums from each column

        # The intersection of these two sets will give us the lucky numbers
        lucky_numbers = list(min_in_rows & max_in_columns)
        return lucky_numbers
        
