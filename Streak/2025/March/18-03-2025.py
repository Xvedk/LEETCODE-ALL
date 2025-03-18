class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 1
        for right, used_bits in enumerate(nums): # used_bits starts as nums[right]
            left = right - 1
            while left >= 0 and used_bits & nums[left] == 0: # while window is valid
                used_bits |= nums[left] # add current num to used_bits, 0 OR 1 = 1
                left -= 1 # move left down

            # left is invalid index, left + 1 is valid. simplify right - (left + 1) + 1
            max_len = max(max_len, right - left)
            
        return max_len
