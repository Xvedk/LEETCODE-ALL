class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        return sorted((lambda c: c.update(dict(nums2)) or c)(Counter(dict(nums1))).items())
