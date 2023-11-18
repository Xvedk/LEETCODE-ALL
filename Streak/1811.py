class Solution(object):
    def maxFrequency(self, nums, k):
        nums.sort()
        n = len(nums)
    
        left = 0
        max_freq = 0
        current_sum = 0

        for right in range(n):
            current_sum += nums[right]

            while (right - left + 1) * nums[right] - current_sum > k:
                current_sum -= nums[left]
                left += 1

            max_freq = max(max_freq, right - left + 1)
        return max_freq
