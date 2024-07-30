class Solution(object):
    def lengthOfLastWord(self, s):
        s = s.strip()  # Remove leading and trailing spaces
        if not s:
            return 0
        
        words = s.split()  # Split the string into words
        return len(words[-1])  # Return the length of the last word
        