class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        # Step 1: Count occurrences in both arrays
        count1 = {}
        count2 = {}
        
        for word in words1:
            count1[word] = count1.get(word, 0) + 1
        
        for word in words2:
            count2[word] = count2.get(word, 0) + 1
        
        # Step 2: Count words that appear exactly once in both arrays
        result = 0
        for word in count1:
            if count1[word] == 1 and count2.get(word, 0) == 1:
                result += 1
        
        return result

