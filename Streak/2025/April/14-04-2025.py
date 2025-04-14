class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        n = len(arr)
        count = 0
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    if ( abs(arr[i] - arr[j]) <= a and 
                    abs(arr[j] - arr[k]) <= b and 
                    abs(arr[i] - arr[k]) <= c ):
                        count += 1
        return count




# class Solution:
#     def countGoodTriplets(self, nums: List[int], a: int, b: int, c: int) -> int:
#         n = len(nums)
#         count = 0
#         i = 0
#         j = i + 1
#         k = j + 1
#         while i + 2 < n:            
#             count += (abs(nums[j] - nums[i]) <= a and
#                 abs(nums[k] - nums[j]) <= b and
#                 abs(nums[k] - nums[i]) <= c)
#             if k < n:
#                 k += 1
#                 if k == n:
#                     j += 1
#                     k = j + 1
#                     if j + 1 == n:
#                         i += 1
#                         j = i + 1
#                         k = j + 1
#         return count
