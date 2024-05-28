class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        left = 0
        currentCost = 0
        maxLength = 0
        
        for right in range(len(s)):
            currentCost += abs(ord(s[right]) - ord(t[right]))
            
            while currentCost > maxCost:
                currentCost -= abs(ord(s[left]) - ord(t[left]))
                left += 1
                
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength
