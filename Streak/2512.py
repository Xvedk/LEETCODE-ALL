class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)

        # Edge case: an empty string or a string starting with '0' cannot be decoded
        if n == 0 or s[0] == '0':
            return 0

        # Initialize an array to store the number of ways to decode the string up to each index
        dp = [0] * (n + 1)
        dp[0] = 1  # Empty string has one way of decoding

        # Iterate through the string
        for i in range(1, n + 1):
            # Check if the current digit is not '0'
            if s[i - 1] != '0':
                dp[i] += dp[i - 1]

            # Check if the previous two digits form a valid mapping
            if i > 1 and '10' <= s[i - 2:i] <= '26':
                dp[i] += dp[i - 2]

        return dp[n]
