class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = {} # Holds answer groups and count in each group.
        total = 0
        
        for answer in answers:
            if answer == 0: total += 1 # unique rabbit
            elif answer in count and count[answer] > 0: count[answer] -= 1  # Same answer, remove questioned rabbit from answer group.  
            
            # New answer or answer count is 0, update total and reset answer count
            else:
                total += answer + 1  # Total increment by answer and questioned rabbit. 
                count[answer] = answer  # Answer has count of answer. Decrement if same answer given later. 
        
        return total

