class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped_anagrams = {}
    
        # Iterate through each string in the array
        for word in strs:
            # Sort the characters of the word to get its unique representation
            sorted_word = ''.join(sorted(word))
            
            # Check if the sorted word is already a key in the dictionary
            if sorted_word in grouped_anagrams:
                # If yes, append the original word to the list of values
                grouped_anagrams[sorted_word].append(word)
            else:
                # If not, create a new key-value pair with the sorted word as key
                # and a list containing the original word as the value
                grouped_anagrams[sorted_word] = [word]
        
        # Extract the grouped anagrams and return them as the final result
        return list(grouped_anagrams.values())
