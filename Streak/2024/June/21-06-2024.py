class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        cur_benefit = sum(customers[:minutes])
        max_benefit = cur_benefit
        optimal_start = 0
        for start in range(1, len(customers) - minutes + 1):
            end = start + minutes - 1
            if grumpy[start-1] == 1:
                cur_benefit -= customers[start-1]
            if grumpy[end] == 1:
                cur_benefit += customers[end]
                if cur_benefit > max_benefit:
                    max_benefit = cur_benefit
                    optimal_start = start
        base_satisfy = 0
        for i in range(len(customers)):
            if grumpy[i] == 0 or optimal_start <= i < optimal_start + minutes:
                base_satisfy += customers[i]
        return base_satisfy
