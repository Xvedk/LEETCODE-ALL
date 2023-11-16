from itertools import product
from typing import List

class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums[0])

        # Generate all possible binary strings of length n
        all_binary_strings = [''.join(seq) for seq in product('01', repeat=n)]

        # Check each binary string against nums
        for binary_string in all_binary_strings:
            if binary_string not in nums:
                return binary_string
