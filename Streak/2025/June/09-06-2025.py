class Solution:
    def findKthNumber(self, n: int, k: int) -> int:
        prefix_res = 1

        while k != 1:
            
            prefix_count = 0
            num_from = prefix_res
            num_to = prefix_res + 1

            while num_from <= n:
                    if n < num_to:
                        prefix_count += n + 1 - num_from
                    else:
                        prefix_count += num_to - num_from

                    num_from *= 10
                    num_to *= 10

            if k > prefix_count:
                prefix_res += 1
                k -= prefix_count
            else:
                prefix_res *= 10
                k -= 1

        return prefix_res

