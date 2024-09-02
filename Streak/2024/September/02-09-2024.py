class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        return bisect_right(p := [*accumulate(chalk)], k % p[-1])      
