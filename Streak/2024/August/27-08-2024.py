class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        dist = [-float('inf')] * n # Array for distances
        adj = defaultdict(list) # Adjacency matrix

        for i, edge in enumerate(edges):
            u, v = edge
            adj[u].append((v, succProb[i]))
            adj[v].append((u, succProb[i]))
        
        pq = [(-1, start_node)] # Max Heap - Start at start_node 
        dist[start_node] = 0  # Distance from start_node to itself

        while pq:
            prob, node = heapq.heappop(pq)
            prob = -prob
            if node == end_node: # If we found end_node
                return prob
            for neighbor, cost in adj[node]:
                newProb = prob * cost # Multiply for the new probability
                if newProb > dist[neighbor]: # Only add to the heap if new distance is greater than previous
                    dist[neighbor] = newProb
                    heapq.heappush(pq, (-newProb, neighbor))
        
        return 0 # If no path from start_node to end_node
