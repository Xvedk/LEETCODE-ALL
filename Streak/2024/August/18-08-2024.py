class Solution:
    def nthUglyNumber(self, n: int) -> int:
        p2, p3, p5 = 0, 0, 0
        ugly = [1]

        for i in range(n-1):
            nextUgly = min(ugly[p2]*2, ugly[p3]*3, ugly[p5]*5)
            ugly.append(nextUgly)

            if nextUgly == ugly[p2]*2:
                p2 += 1
            if nextUgly == ugly[p3]*3:
                p3 += 1
            if nextUgly == ugly[p5]*5:
                p5 += 1
        return ugly[-1]
