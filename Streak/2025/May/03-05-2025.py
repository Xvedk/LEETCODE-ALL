class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        # Try making every tile show 'target' on one row; return min flips or -1 if impossible
        def check(target: int) -> int:
            top_flips, bottom_flips = 0, 0
            for t, b in zip(tops, bottoms):
                if t != target and b != target:
                    # Neither side matches target → fail
                    return -1           
                if t != target:
                    # Flip this tile’s top to target
                    top_flips += 1      
                elif b != target:
                    # Flip this tile’s bottom to target
                    bottom_flips += 1   
            return min(top_flips, bottom_flips)

        # First candidate: tops[0]
        res = check(tops[0])
        # If it works, or tops[0] == bottoms[0] (same candidate), return result
        if res != -1 or tops[0] == bottoms[0]:
            return res
        # Otherwise try bottoms[0]
        return check(bottoms[0])
