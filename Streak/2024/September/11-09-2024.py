class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        start_bin, goal_bin = bin(start)[2:], bin(goal)[2:]
        if len(start_bin) < len(goal_bin):
            start_bin = "0"* (len(goal_bin) - len(start_bin)) + start_bin
        if len(goal_bin) < len(start_bin):
            goal_bin = "0"* (len(start_bin) - len(goal_bin)) + goal_bin
        ans = 0
        print(f"start {start_bin} end {goal_bin}")
        for s, g in zip(start_bin, goal_bin):
            if s != g:
                ans += 1
        return ans

# With Bit Manipulation .. Optimized version
    # def minBitFlips(self, start: int, goal: int) -> int:
    #     # XOR of same no is 0 else 1
    #     xor = start ^ goal
    #     ans = 0
    #     while xor:
    #         ans += xor&1   # taking last bit if 1 then +1 else +0
    #         xor >>= 1
    #     return ans
