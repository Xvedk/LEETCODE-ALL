class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        xor = 0
        for num in nums:
            xor ^= num
        right_bit = xor & -xor
        n1, n2 = 0, 0
        for num in nums:
            if num & right_bit:
                n1 ^= num
            else:
                n2 ^= num
        return[n1,n2]
