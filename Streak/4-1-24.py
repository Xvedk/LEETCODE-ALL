class Solution:
    def minOperations(self, nums: List[int]) -> int:
        foo = Counter(nums)
        result = 0
        for value in foo.values():
            if value == 1:
                return -1
            else:
                if value%3 == 0:
                    result += value//3 
                else:
                    result += value//3 + 1
        return result
