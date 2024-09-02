class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        # Initialize a frequency dictionary for both strings
        frequency_s = {}
        frequency_t = {}
        
        # Count the frequency of each character in s
        for char in s:
            frequency_s[char] = frequency_s.get(char, 0) + 1
            
        # Count the frequency of each character in t
        for char in t:
            frequency_t[char] = frequency_t.get(char, 0) + 1
            
        # Compare the frequency dictionaries to find the added character
        for char in frequency_t:
            if frequency_t[char] != frequency_s.get(char, 0):
                return char
