class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Sort the tiles to help skip duplicates during recursion.
        tiles = sorted(tiles)
        ans = set()
        
        def backtrack(curr, used):
            # If curr is not empty, add the formed sequence to ans.
            if curr:
                ans.add("".join(curr))
            
            for i in range(len(tiles)):
                # Skip this tile if it has already been used.
                if used[i]:
                    continue
                # Skip duplicates: if the current tile is the same as the previous one
                # and the previous one wasn't used in this recursion branch,
                # then skip to avoid duplicate sequences.
                if i > 0 and tiles[i] == tiles[i - 1] and not used[i - 1]:
                    continue
                
                used[i] = True
                curr.append(tiles[i])
                backtrack(curr, used)
                curr.pop()
                used[i] = False
        
        # Initialize a used array for the tiles.
        used = [False] * len(tiles)
        backtrack([], used)
        
        return len(ans)
