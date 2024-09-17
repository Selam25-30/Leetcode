from typing import List

class Solution:
    def numberOfLines(self, widths: List[int], s: str) -> List[int]:
        # Define constants
        MAX_WIDTH = 100
        
        # Initialize variables
        lines = 1
        current_width = 0
        
        # Iterate over each character in the string
        for char in s:
            char_width = widths[ord(char) - ord('a')]
            if current_width + char_width > MAX_WIDTH:
                # If adding the character exceeds the line width, start a new line
                lines += 1
                current_width = char_width
            else:
                # Otherwise, add the character to the current line
                current_width += char_width
        
        return [lines, current_width]
