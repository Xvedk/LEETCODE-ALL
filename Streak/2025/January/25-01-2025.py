class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        new=[]
        for i in range(len(nums)):
            new.append([nums[i],i])
        new=sorted(new,key=lambda x:x[0])
        new2d=[[new[0]]]
        for i in range(1,len(nums)):
            if new[i][0]-new[i-1][0]<=limit:
                new2d[-1].append(new[i])
            else:
                new2d.append([new[i]])
        for v in new2d:
            index=[]
            for m,n in v:
                index.append(n)
            index.sort()
            for i in range(len(index)):
                nums[index[i]]=v[i][0]
        return nums
