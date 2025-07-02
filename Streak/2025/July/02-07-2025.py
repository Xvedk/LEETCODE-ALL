class Solution:
    def possibleStringCount(self, word: str, k: int) -> int:
        mod: int = 10**9 + 7

        island_sizes: list[int] = []
        tmp_count: int = 1
        for i in range(len(word) - 1):
            if word[i] == word[i+1]:
                tmp_count += 1
            else:
                island_sizes.append(tmp_count)
                tmp_count = 1
        island_sizes.append(tmp_count)

        total_number_of_words: int = 1
        for island_size in island_sizes:
            total_number_of_words *= island_size
            total_number_of_words %= mod

        if len(island_sizes) >= k:
            # k = 5, word = aabbccaabbcc. The smallest word we can make is abcabc which is length 6.
            return total_number_of_words

        # dp[i][j] => represents the number of words of length exactly j using island_sizes[:i]
        dp: list[list[int]] = [[0 for _ in range(k)] for _ in range(len(island_sizes) + 1)]  # k^2 size

        # Initialization
        dp[0][0] = 1  # there is one way of making a word of size 0 with 0 islands
        # dp[i][0] = 0 when i > 0 because there is no way of making a word of size 0 with i > 0 islands

        # Transition
        for i in range(1, len(island_sizes) + 1):
            prefix_sum_dp_i_minus_1: list[int] = [
                0
            ] * (k + 1)  # prefix_sum_dp_i_minus_1[j] = sum(everything up to j, j excluded)
            for j in range(k):
                prefix_sum_dp_i_minus_1[j+1] = (prefix_sum_dp_i_minus_1[j] + dp[i-1][j]) % mod

            for j in range(k):
                dp[i][j] = (prefix_sum_dp_i_minus_1[j] - prefix_sum_dp_i_minus_1[j - min(j, island_sizes[i-1])]) % mod


        return (total_number_of_words - sum(dp[len(island_sizes)][j] for j in range(k))) % mod
