class MyCalendarTwo:
    def __init__(self):
        self.mp = defaultdict(int)
    def book(self, start: int, end: int) -> bool:
        self.mp[start] += 1
        self.mp[end] -= 1

        ActiveCount = 0
        for value, count in sorted(self.mp.items()):
            ActiveCount += count
            if ActiveCount > 2:
                self.mp[start] -= 1
                self.mp[end] += 1
                return False
        return True
