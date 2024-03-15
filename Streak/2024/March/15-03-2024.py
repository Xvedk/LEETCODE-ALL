from collections import deque
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        m={}
        result=deque()
        for i in nums:
            m[i]=m.get(i,0)+1
        def fun(m,nums,result,z=0,sum1=1,x=len(nums)):
            if z>x-1:
                return result
            curr=nums[z]
            for i in m:
                if i !=curr:
                    sum1=sum1*(i**m[i]) 
                elif i==curr and m[i]>=2:
                    sum1=sum1*(i**(m[i]-1)) 
            result.append(sum1)
            return fun(m,nums,result,z+1)
        return fun(m,nums,result)

