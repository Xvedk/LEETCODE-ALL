class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        power = 14 # max power is 14, 3^15 = ~14 mil and n <= 10^7 or 10 mil
        while power >= 0 and n > 0:
            num = pow(3, power)
            if n >= num:
                n -= num # sum always has num if < remaining n
            power -= 1 # go to next power

        return n == 0 # n - sum of powers = 0
