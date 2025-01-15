class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        num_set_bits1, num_set_bits2 = bin(num1).count('1'), bin(num2).count('1')
        res = 0

        if num_set_bits1 == num_set_bits2:
            return num1
        elif num_set_bits1 > num_set_bits2:
            diff = num_set_bits1 - num_set_bits2
            i = 0
            while diff > 0:
                b = 1 if num1 & (1 << i) > 0 else 0
                if b == 1:
                    diff -= 1
                    num1 = num1 ^ (1 << i)
                i += 1
            
            return num1
        
        else:
            diff = num_set_bits2 - num_set_bits1
            i = 0
            while diff > 0:
                b = 1 if num1 & (1 << i) > 0 else 0
                if b == 0:
                    diff -= 1
                    num1 = num1 | (1 << i)
                i += 1
            
            return num1
