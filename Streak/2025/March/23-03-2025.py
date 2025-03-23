class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        MOD = pow(10, 9) + 7
        roadArr = [[] for _ in range(n)]
        for u, v, t in roads:
            roadArr[u].append((v, t))
            roadArr[v].append((u, t)) # bug1: bi-directional instead of directional

        # improve: countDict can use array (0 to n - 1 is consequetive)
        heap, countDict, reachTime = [(0, 0, -1)], {-1:(0, 1)}, sys.maxsize # heap: time (accumulated sum), node index, prev_node_index || dict: node index: (sumTime, count)
        while len(heap) and heap[0][0] <= reachTime:
            sumTime, index, preNodeIndex = heapq.heappop(heap)
            if index in countDict:
                if sumTime == countDict[index][0]:
                    countDict[index] = (sumTime, (countDict[index][1] + countDict[preNodeIndex][1]) % MOD) # update count, bug2 use preNodeIndex instead of 1
                continue

            countDict[index] = (sumTime, countDict[preNodeIndex][1])
            for nextIndex, time in roadArr[index]:
                if nextIndex in countDict:
                    if time + sumTime > countDict[nextIndex][0]:
                        continue
                if nextIndex == n - 1:
                    reachTime = min(time + sumTime, reachTime)
                if sumTime + time <= reachTime:
                    heapq.heappush(heap, (sumTime + time, nextIndex, index)) # bug2: preNodeIndex, index and nextIndex 
            # print(sumTime, index, preNodeIndex, countDict)
            # print(heap)
        return countDict[n - 1][1]
                    
      
