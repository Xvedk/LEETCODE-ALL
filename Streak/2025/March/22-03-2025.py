class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = list(range(n))
        rank = [1] * n

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x == root_y:
                return
            if rank[root_x] < rank[root_y]:
                parent[root_x] = root_y
            elif rank[root_x] > rank[root_y]:
                parent[root_y] = root_x
            else:
                parent[root_y] = root_x
                rank[root_x] += 1

        for u, v in edges:
            union(u, v)

        comp_size = [0] * n
        comp_edges = [0] * n

        for i in range(n):
            comp_size[find(i)] += 1

        for u, v in edges:
            comp_edges[find(u)] += 1

        count = 0
        for i in range(n):
            if find(i) == i:
                if comp_edges[i] == comp_size[i] * (comp_size[i] - 1) // 2:
                    count += 1

        return count
