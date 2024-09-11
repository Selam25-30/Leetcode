class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Create a list of (score, index) and sort it in descending order of score
        sorted_scores = sorted([(s, i) for i, s in enumerate(score)], reverse=True, key=lambda x: x[0])
        
        # Initialize an answer array with the same length as score
        answer = [""] * len(score)
        
        # Assign medals or ranks based on the sorted order
        for rank, (s, i) in enumerate(sorted_scores):
            if rank == 0:
                answer[i] = "Gold Medal"
            elif rank == 1:
                answer[i] = "Silver Medal"
            elif rank == 2:
                answer[i] = "Bronze Medal"
            else:
                answer[i] = str(rank + 1)
        
        return answer
