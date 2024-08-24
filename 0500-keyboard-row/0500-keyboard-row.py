class Solution:
    def findWords(self, words: list[str]) -> list[str]:
        # Define sets for each row
        row1 = set("qwertyuiop")
        row2 = set("asdfghjkl")
        row3 = set("zxcvbnm")
        
        def can_be_typed_on_one_row(word: str) -> bool:
            # Convert word to lowercase to handle both cases
            word = word.lower()
            # Determine the row of the first character
            if word[0] in row1:
                row = row1
            elif word[0] in row2:
                row = row2
            elif word[0] in row3:
                row = row3
            else:
                return False
            
            # Check if all characters in the word belong to the same row
            return all(char in row for char in word)
        
        # Filter and return the words that can be typed using one row
        return [word for word in words if can_be_typed_on_one_row(word)]
