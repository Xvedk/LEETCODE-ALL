class Solution:
    def longestSubsequenceRepeatedK(self, s: str, k: int) -> str:
        # Helper function to check if `sub` appears at least `k` times in `t`
        def isK(sub: str, t: str, k: int) -> bool:
            count = 0  # Counts how many full repetitions of `sub` are found
            i = 0      # Tracks the current position in `sub`
            
            # Iterate through each character in `t`
            for ch in t:
                # If the current character matches `sub[i]`
                if i < len(sub) and ch == sub[i]:
                    i += 1  # Move to the next character in `sub`
                    
                    # If we've matched all characters in `sub`
                    if i == len(sub):
                        i = 0       # Reset to start of `sub`
                        count += 1   # Increment repetition count
                        
                        # If we've found `k` repetitions, return True
                        if count == k:
                            return True
            # If we exit the loop without finding `k` repetitions, return False
            return False

        # Initialize the result as an empty string
        res = ""
        
        # Use a queue for BFS (Breadth-First Search) to explore possible subsequences
        q = deque([""])  # Start with an empty string
        
        # Process each candidate subsequence in the queue
        while q:
            curr = q.popleft()  # Get the next candidate
            
            # Try appending each lowercase letter ('a' to 'z') to `curr`
            for ch in map(chr, range(ord('a'), ord('z') + 1)):
                nxt = curr + ch  # Form a new candidate by adding `ch`
                
                # Check if `nxt` appears at least `k` times in `s`
                if isK(nxt, s, k):
                    res = nxt      # Update the result (longest valid subsequence found so far)
                    q.append(nxt)  # Add to queue for further exploration (longer subsequences)
        
        # Return the longest valid subsequence found
        return res
