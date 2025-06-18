class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()
        result = []
        for i in range(0,len(nums),3): 
            if abs(nums[i]-nums[i+2]) > k: 
                return []
            result.append(nums[i:i+3])
        return result
