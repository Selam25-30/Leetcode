from typing import List

class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        
        for op in operations:
            if op == 'C':
                # Invalidate the previous score
                if record:
                    record.pop()
            elif op == 'D':
                # Double the last score
                if record:
                    record.append(2 * record[-1])
            elif op == '+':
                # Add the sum of the last two scores
                if len(record) >= 2:
                    record.append(record[-1] + record[-2])
            else:
                # Record a new score (it should be a number)
                record.append(int(op))
        
        # Return the sum of all recorded scores
        return sum(record)

# Example usage:
sol = Solution()
# print(sol.calPoints(["5", "2", "C", "D", "+"]))  # Output: 30
# print(sol.calPoints(["5", "-2", "4", "C", "D", "9", "+", "+"]))  # Output: 27
# print(sol.calPoints(["1", "C"]))  # Output: 0
