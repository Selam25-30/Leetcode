from collections import Counter

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Count frequency of characters in chars
        char_count = Counter(chars)
        total_length = 0
        
        # Check each word in words
        for word in words:
            word_count = Counter(word)
            # Check if the word can be formed by comparing counts
            can_form = True
            for char, count in word_count.items():
                if char_count[char] < count:
                    can_form = False
                    break
            # If the word can be formed, add its length to total
            if can_form:
                total_length += len(word)
        
        return total_length
