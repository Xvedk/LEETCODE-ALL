class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        adjs=collections.defaultdict(set)
        for i,j in adjacentPairs:
            adjs[i].add(j)
            adjs[j].add(i)

        for node,adj in adjs.items():
            if len(adj)==1:
                break
        ans=[node]
        while adjs[node]:
            new=adjs[node].pop()
            ans.append(new)
            adjs[new].remove(node)
            node=new
        return ans    
