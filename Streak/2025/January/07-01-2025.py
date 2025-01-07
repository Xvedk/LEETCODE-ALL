
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        # Sort the list of words by their lengths (shorter words first)
        words.sort(key=len)  
        ans = []  # Initialize the result list to store matching substrings

        # Iterate over each word in the list
        for i in range(len(words)):
            # Compare the current word with all subsequent longer words
            for j in range(i + 1, len(words)):  
                # Check if the current word is a substring of the longer word
                if words[i] in words[j]:
                    ans.append(words[i])  # Add the word to the result list
                    break  # Break early as the word is already matched

        # Return the list of substrings found
        return ans 
