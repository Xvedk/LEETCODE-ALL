import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.limit = k
        self.top_elements = []
        for num in nums:
            self.add_element(num)

    def add(self, val: int) -> int:
        return self.add_element(val)

    def add_element(self, new_val: int) -> int:
        if len(self.top_elements) < self.limit:
            heapq.heappush(self.top_elements, new_val)
        elif new_val > self.top_elements[0]:
            heapq.heapreplace(self.top_elements, new_val)
        
        return self.top_elements[0] if self.top_elements else 0
