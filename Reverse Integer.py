class Solution:
    def reverse(self, x: int) -> int:
        isNeg = False
        arr = []
        b = ""
        if len(str(x)) == 1:
            return x
        while x % 10 == 0:
            x = int(x / 10)
        if x < 0:
            isNeg = True
            x *= -1
        for i in str(x):
            arr.append(i)
        for j in arr[::-1]:
            b += j
        c = int(b)
        if isNeg:
            c *= -1
        if c.bit_length() > 31:
            return 0
        else:
            return c
