class Solution:
    def sortColors(self, nums: List[int]) -> None:

        count_zeros = 0
        count_ones = 0
        count_twos = 0


        for i in nums:
            if i == 0:
                count_zeros = count_zeros + 1
            elif i == 1:
                count_ones = count_ones + 1
            elif i == 2:
                count_twos = count_twos + 1

        nums[:] = []

        for i in range(count_zeros):
            nums.append(0)

        for i in range(count_ones):
            nums.append(1)

        for i in range(count_twos):
            nums.append(2)
