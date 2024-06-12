class Solution:
    def sortColors(self, l: List[int]) -> None:
        n=len(l)
        for i in range(n-1):
            for j in range(i+1,n):
                if(l[i]>l[j]):
                    l[i],l[j]=l[j],l[i]
