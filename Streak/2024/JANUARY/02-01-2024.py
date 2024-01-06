class Solution:
    def findMatrix(self, l: List[int]) -> List[List[int]]:
        k=[]
        while l:
            s=[]
            m=set(l)
            for i in m:
                s.append(i)
                l.remove(i)
            k.append(s)
        return (k) 
