class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        if p == 0:
            return 0

        nums.sort()
        n = len(nums)

        # Special case: max possible pairs
        if p * 2 == n:
            max_diff = 0
            for i in range(0, n - 1, 2):
                max_diff = max(max_diff, nums[i + 1] - nums[i])
            return max_diff

        # Precompute adjacent differences
        differences = [nums[i] - nums[i - 1] for i in range(1, n)]

        # Check if we can form at least p non-overlapping pairs with max diff <= dmax
        def canFormPairs(dmax: int) -> bool:
            i = 0
            pairs = 0
            while i < len(differences) and pairs < p:
                if differences[i] <= dmax:
                    pairs += 1
                    i += 2  # skip next to avoid overlapping
                else:
                    i += 1
            return pairs >= p

        # Binary search the minimum possible dmax
        left, right = 0, max(differences)
        while left < right:
            mid = (left + right) // 2
            if canFormPairs(mid):
                right = mid
            else:
                left = mid + 1

        return left
