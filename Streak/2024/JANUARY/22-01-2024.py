class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        orig = sum(nums) - sum(set(nums))
        diff = (len(nums)*(len(nums)+1))//2 - sum(nums)
        return [orig, orig + diff]
