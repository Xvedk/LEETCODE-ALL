class Solution(object):
    def reductionOperations(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_num = max(nums)
        freq = [0] * (max_num + 1)

        for num in nums:
            freq[num] += 1

        operations = 0
        result = 0

        for i in range(max_num, 0, -1):
            if freq[i] > 0:
                operations += freq[i]
                result += operations - freq[i]

        return result
