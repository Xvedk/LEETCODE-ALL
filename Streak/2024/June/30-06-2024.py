class DS:
    def __init__(self, n: int):
        self.n = n
        self.n_set = n
        self.parent = list(range(n))
    
    def find_root(self, v: int) -> int:
        if self.parent[v] == v:
            return v
        self.parent[v] = self.find_root(self.parent[v])
        return self.parent[v]

    def join(self, u: int, v: int) -> bool:
        if self.n_set == 1:
            return False
        u_root = self.find_root(u)
        v_root = self.find_root(v)
        if u_root == v_root:
            return False
        self.parent[u_root] = v_root
        self.n_set -= 1
        return True
        
class Solution:
    def maxNumEdgesToRemove(self, n: int, edges: List[List[int]]) -> int:
        ds_a = DS(n)
        ds_b = DS(n)
        reordered_edges = sorted(edges, key=lambda x: x[0], reverse=True)
        edges_used = 0
        print(reordered_edges)
        # note: node ids start from 1
        for n_type, u, v in reordered_edges:
            if n_type == 3 and ds_a.n_set != 1:
                if ds_a.join(u - 1, v - 1) and ds_b.join(u - 1, v - 1):
                    edges_used += 1
            elif n_type == 1 and ds_a.n_set != 1:
                if ds_a.join(u - 1, v - 1):
                    edges_used += 1
            elif n_type == 2 and ds_b.n_set != 1:
                if ds_b.join(u - 1, v - 1):
                    edges_used += 1

        if ds_b.n_set != 1 or ds_a.n_set != 1:
            return -1
        
        return len(edges) - edges_used
