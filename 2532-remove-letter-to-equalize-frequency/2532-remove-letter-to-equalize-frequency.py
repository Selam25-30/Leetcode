from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        # Get the frequency of each character in the word
        freq = Counter(word)
        
        # Iterate through each character in the word
        for char in word:
            # Decrease the frequency of the current character by 1
            freq[char] -= 1
            
            # If the frequency of a character drops to 0, remove it from the dictionary
            if freq[char] == 0:
                del freq[char]
                
            # Get the set of frequencies left after removing the character
            freq_set = set(freq.values())
            
            # If all frequencies are equal, return True
            if len(freq_set) == 1:
                return True
            
            # Revert the change for the next iteration
            freq[char] += 1
        
        # If no valid removal was found, return False
        return False
