class Solution:
    def triangleType(self, nums: List[int]) -> str:
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    if nums[i]+nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        if nums[i] == nums[j] == nums[k]:
                            return 'equilateral'
                        elif nums[i] == nums[j] or nums[i] == nums[k] or nums[j] == nums[k]:
                            return 'isosceles'
                        else:
                            return 'scalene'
                    else:
                        return 'none'
