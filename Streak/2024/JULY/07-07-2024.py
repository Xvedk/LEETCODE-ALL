class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        s = numBottles
        n = numBottles//numExchange
        while(n > 0):
            n = numBottles // numExchange
            remainder = numBottles % numExchange
            s += n
            numBottles = n+remainder
        return (s)
