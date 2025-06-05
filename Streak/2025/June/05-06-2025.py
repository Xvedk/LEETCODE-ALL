class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        parent = list(range(26)) 

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])  
            return parent[x]

        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX == rootY:
                return
            if rootX < rootY:
                parent[rootY] = rootX
            else:
                parent[rootX] = rootY
        for a, b in zip(s1, s2):
            union(ord(a) - 97, ord(b) - 97)
        result = []
        for c in baseStr:
            result.append(chr(find(ord(c) - 97) + 97))
        return ''.join(result)
