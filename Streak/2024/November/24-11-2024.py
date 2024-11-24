class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total = 0
        neg_count = 0
        min_abs = float('inf')
        for row in matrix:
            for ele in row:
                total += abs(ele)
                neg_count += ele < 0
                min_abs = min(min_abs, abs(ele))
        return total if neg_count % 2 == 0 else total - 2 * min_abs        
