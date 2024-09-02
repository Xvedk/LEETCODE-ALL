class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        
        checked = math.inf
        for i in range(len(nums)):
            left, right = i + 1, len(nums) - 1
            if nums[i] == checked:
                continue
            if left > len(nums) - 2 or nums[i] > 0:
                break

            target = -1 * nums[i]
            seen = set()
            while left < right:
                if nums[left] in seen:
                    left += 1
                    continue
                if nums[right] in seen:
                    right -= 1
                    continue
                summation = nums[left] + nums[right]

                if summation == target:
                    res.append([nums[i], nums[left], nums[right]])
                    seen.add(nums[left])
                    seen.add(nums[right])
                    left += 1
                elif summation > target:
                    right -= 1
                else:
                    left += 1
            checked = nums[i]
        return res
        
