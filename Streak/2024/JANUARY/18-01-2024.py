class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        elif n == 2:
            return 2

        # Initialize an array to store the number of ways for each step
        ways = [0] * n
        ways[0] = 1
        ways[1] = 2

        # Calculate the number of ways for each step from the third step to the top
        for i in range(2, n):
            ways[i] = ways[i-1] + ways[i-2]

        return ways[-1]
