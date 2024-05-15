class Solution:
    def valid(self, i: int, j: int, n: int) -> bool:
        return 0 <= i < n and 0 <= j < n

    def compute_distance_grid(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        dist_grid = [[float('inf')] * n for _ in range(n)]
        q = deque()

        # Initialize the queue and distance for '0' cells
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i, j))
                    dist_grid[i][j] = 0

        # Directions: up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # BFS to compute minimum distances
        while q:
            x, y = q.popleft()
            for dx, dy in directions:
                new_x, new_y = x + dx, y + dy
                if self.valid(new_x, new_y, n) and dist_grid[new_x][new_y] == float('inf'):
                    dist_grid[new_x][new_y] = dist_grid[x][y] + 1
                    q.append((new_x, new_y))

        return dist_grid

    def maximumSafenessFactor(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[n - 1][n - 1] == 1 or grid[0][0] == 1:
            return 0

        dist = self.compute_distance_grid(grid)
        pq = []
        vis = [[0] * n for _ in range(n)]

        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        heapq.heappush(pq, (-dist[0][0], 0, 0))
        vis[0][0] = 1

        while pq:
            ds, i, j = heapq.heappop(pq)
            ds = -ds

            if i == n - 1 and j == n - 1:
                return ds

            for dx, dy in directions:
                new_row, new_col = i + dx, j + dy
                if self.valid(new_row, new_col, n) and grid[new_row][new_col] != 1 and not vis[new_row][new_col]:
                    vis[new_row][new_col] = 1
                    new_ds = dist[new_row][new_col]
                    heapq.heappush(pq, (-min(ds, new_ds), new_row, new_col))

        return 0
