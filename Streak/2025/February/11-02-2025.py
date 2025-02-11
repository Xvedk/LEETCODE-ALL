class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        stack = ""
        part_size = len(part)
        for i in s:
            stack += i
            if stack[len(stack)-part_size:] == part:
                stack = stack[:len(stack)-part_size]
        return stack
