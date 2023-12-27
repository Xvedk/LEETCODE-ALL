class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        
        time = 0
        if len(colors) == 1:
            return time
        
        
        for i in range(len(colors)-1):
            curColor = colors[i]
            nextColor = colors[i+1]
			
            if curColor == nextColor:
                if neededTime[i] < neededTime[i+1]:
                    time += neededTime[i]
                else:
                    time += neededTime[i+1]
                    neededTime[i+1], neededTime[i] = neededTime[i], neededTime[i+1]
                
        
        return time
