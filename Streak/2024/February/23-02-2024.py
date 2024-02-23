
class Solution:
    #pq elements: (dist, stop_num, )
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        gr=[[] for i in range(n)]
        price=[[1000001,n+1] for i in range(n)]
        for f in flights:
            gr[f[0]].append((f[1],f[2]))
        pq=[(0,0,src)]
        while len(pq):
            pr,st,node=heappop(pq)
            if node==dst:
                return pr
            if st>k:
                continue
            for ch in gr[node]:
                if (price[ch[0]][0]>pr+ch[1] or price[ch[0]][1]>st+1):
                    price[ch[0]][0]=pr+ch[1]
                    price[ch[0]][1]=st+1
                    heappush(pq,(pr+ch[1],st+1,ch[0]))
        return -1
