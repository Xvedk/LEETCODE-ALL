class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        m = len(grid)
        n = len(grid[0])
        arr = []
        remain = grid[0][0] % x


        for i in range(m):
            for j in range(n):
                if grid[i][j] % x != remain:
                    return -1
                arr.append(grid[i][j])

        arr.sort()

        median = arr[len(arr) // 2]
        operations = 0
        for num in arr:
            operations += abs(num - median) // x

        return operations

        
