class Solution:
    def minimumLength(self, s: str) -> int:
        c = Counter(s)
        num_deleted = 0

        for val in c.values():
            if val > 2:
                num_deleted += val - (2 if val & 1 == 0 else 1)

        return len(s) - num_deleted
