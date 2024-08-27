from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: list[str]) -> str:
        # Step 1: Filter and count relevant letters in licensePlate
        license_counter = Counter(char.lower() for char in licensePlate if char.isalpha())
        
        # Step 2: Find the shortest completing word
        shortest_word = None
        for word in words:
            word_counter = Counter(word)
            
            # Check if word can be a completing word
            if all(word_counter[char] >= count for char, count in license_counter.items()):
                if shortest_word is None or len(word) < len(shortest_word):
                    shortest_word = word
        
        return shortest_word

# Example usage:
solution = Solution()
print(solution.shortestCompletingWord("1s3 PSt", ["step","steps","stripe","stepple"]))  # Output: "steps"
print(solution.shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))  # Output: "pest"
