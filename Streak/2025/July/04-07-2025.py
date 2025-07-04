class Solution:
    def kthCharacter(self, k: int, operations: List[int]) -> str:
        k -= 1
        res = 0

        for i in range(min(len(operations), 60)):
            if (k >> i) & 1:
                res += operations[i]

        return chr((res % 26) + ord('a'))
