import re
from collections import Counter

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        # Step 1: Normalize the paragraph to lowercase and remove punctuation
        words = re.findall(r'\w+', paragraph.lower())
        
        # Step 2: Create a set of banned words for quick lookup
        banned_set = set(banned)
        
        # Step 3: Count the frequency of each word
        word_count = Counter(word for word in words if word not in banned_set)
        
        # Step 4: Return the most common word that is not banned
        return word_count.most_common(1)[0][0]
