class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # we can just focus on distinct numbers in $nums$

        # in example 1, d = {5, 4, 2}
        # we can see that the numbers > 2 are 5 and 4, so the answer is 2
        # in op1, we can choose h = 4 to make [5,2,5,4,5] to [4,2,4,4,4]
        # in op2, we can choose h = 2 to make [4,2,4,4,4] to [2,2,2,2,2]

        # in example 2, d = {1, 2}
        # since 1 < 2 so it is not possible to make all elements equal to k,
        # hence we return -1 in this case

        # if there is a number $x$ that is less than $k$,
        # then return -1
        if any(x < k for x in nums): return -1
        # otherwise check the size of the unique number that is greater than k
        return len(set(x for x in nums if x > k))
