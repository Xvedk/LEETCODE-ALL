class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        d={}
        l=[]
        for i in nums:
            d[i]=d.get(i,0)+1
        for p,q in d.items():
            l.append(q)
        a=max(l)
        s=0
        for i in l:
            if i==a:
                s=s+a
        return s
