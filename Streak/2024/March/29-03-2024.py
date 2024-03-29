class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        maxi = 1
        n = len(nums)
        for i in range(n):
            maxi = max(maxi, nums[i])
        
        count, total, left, right = 0, 0, 0, 0
        while right<n:
            if nums[right] == maxi:
                count += 1
            if count == k:
                total += (n-right)
                while left<=right and count==k:
                    if nums[left] == maxi:
                        count -= 1
                    left += 1
                    if count == k:
                        total += (n-right)
                    else:
                        break
            right += 1

        return total
