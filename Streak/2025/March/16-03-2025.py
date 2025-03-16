class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        minr=min(ranks)
        maxr=max(ranks)
        n=len(ranks)
        freq=[0]*(maxr+1)
        for rank in ranks:
            minr=min(rank,minr)
            freq[rank]+=1
        l=1
        r=minr*cars**2
        while l<r:
            m=(l+r)//2
            s=0
            for i in range(1,maxr+1):
                s+=freq[i]int((m//i)*(1/2))
            if int(s)>=cars:
                r=m
            else:
                l=m+1
        return l
