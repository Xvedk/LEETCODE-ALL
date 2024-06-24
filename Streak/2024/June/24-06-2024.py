class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        current_flips = [0] * (n + 1)
        flips = 0
        
        for i in range(n):
            # Apply the flip effect from k steps back
            flips ^= current_flips[i]
            # Check if we need to flip at this position
            if (nums[i] + flips) % 2 == 0:
                # If flipping here would go out of bounds, return -1
                if i + k > n:
                    return -1
                # Perform the flip
                flip_count += 1
                flips ^= 1
                current_flips[i + k] ^= 1
        
        return flip_count
