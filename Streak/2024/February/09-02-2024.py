class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()  
        arr=[[num]for num in nums]
        for i in range(1,len(nums)):
            for j in range(i):
                if nums[i]%nums[j]==0 and len(arr[i]) < len(arr[j])+1:
                    arr[i]=arr[j]+[nums[i]]
        arr.sort(key=len,reverse=True)
        return arr[0]
