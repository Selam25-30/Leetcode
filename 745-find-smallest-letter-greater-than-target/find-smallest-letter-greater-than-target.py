class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        # Iterate through the letters to find the first one greater than the target
        for letter in letters:
            if letter > target:
                return letter
        # If no letter greater than target is found, return the first letter
        return letters[0]
