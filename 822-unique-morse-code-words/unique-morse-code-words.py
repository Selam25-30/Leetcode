from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        # Define the Morse code for each letter of the alphabet
        morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
                      "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
                      "..-", "...-", ".--", "-..-", "-.--", "--.."]
        
        # Create a mapping from letter to its Morse code
        letter_to_morse = {chr(i + ord('a')): morse_code[i] for i in range(26)}
        
        # Define a set to store unique Morse code transformations
        unique_transformations = set()
        
        # Process each word in the list
        for word in words:
            # Convert each word to its Morse code representation
            morse_representation = ''.join(letter_to_morse[char] for char in word)
            # Add the Morse code representation to the set
            unique_transformations.add(morse_representation)
        
        # The number of unique Morse code transformations
        return len(unique_transformations)
