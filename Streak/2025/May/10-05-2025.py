class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        s1,z1=0,0
        s2,z2=0,0
        for x in nums1:
            if x==0:
                z1+=1
            else:
                s1+=x
        for x in nums2:
            if x==0:
                z2+=1
            else:
                s2+=x
        sum1=s1+z1
        sum2=s2+z2
        if z1==0 and s1<sum2:
            return -1
        if z2==0 and s2<sum1:
            return -1
        return max(sum1,sum2) 
