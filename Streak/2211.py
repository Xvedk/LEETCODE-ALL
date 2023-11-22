class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        mp,ans={},[]
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if i+j not in mp:mp[i+j]=[nums[i][j]]
                else:mp[i+j].append(nums[i][j])
        for i in mp:ans.extend(mp[i][::-1])
        return ans
