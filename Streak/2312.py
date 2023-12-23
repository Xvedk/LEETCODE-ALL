class Solution(object):
    def isPathCrossing(self, path):
        """
        :type path: str
        :rtype: bool
        """
        # Initialize the current position
        x, y = 0, 0
        # Initialize a set to store visited positions
        visited = {(x, y)}
        
        # Define the directions for moving
        directions = {'N': (0, 1), 'S': (0, -1), 'E': (1, 0), 'W': (-1, 0)}
        
        # Iterate through the path and update the position
        for move in path:
            dx, dy = directions[move]
            x, y = x + dx, y + dy
            
            # Check if the current position has been visited before
            if (x, y) in visited:
                return True
            
            # Add the current position to the set of visited positions
            visited.add((x, y))
        
        # If the path doesn't cross itself, return False
        return False
