class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.rank = [0] * (n+1)
        self.value = [-1] * (n+1)
    
    def find(self,x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x
    
    def combine(self,x,y,w):
        p_x, p_y = self.find(x), self.find(y)
        if p_x == p_y:
            self.value[p_x] &= w
            return
        if self.rank[p_x] > self.rank[p_y]:
            self.value[p_x] &= (self.value[p_y] & w) if self.value[p_y] != -1 else w
            self.parent[p_y] = p_x
        elif self.rank[p_x] < self.rank[p_y]:
            self.value[p_y] &= (self.value[p_x] & w) if self.value[p_x] != -1 else w
            self.parent[p_x] = p_y
        else:
            self.parent[p_y] = p_x
            self.rank[p_x] += 1
            self.value[p_x] &= (self.value[p_y] & w) if self.value[p_y] != -1 else w
    
    def getPath(self,x):
        return self.value[self.find(x)]


class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        dsu = DSU(n)

        for u,v,w in edges:
            dsu.combine(u,v,w)
        
        ans = []
        for u,v in query:
            if dsu.find(u) == dsu.find(v):
                ans.append(dsu.getPath(u))
            else:
                ans.append(-1)

        return ans
