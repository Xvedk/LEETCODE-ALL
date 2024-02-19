class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
            # 0b1 0000...0000 <- always a power of 2
        if '1' in str(bin(n))[3:]:
            return False
        else:
            return True
