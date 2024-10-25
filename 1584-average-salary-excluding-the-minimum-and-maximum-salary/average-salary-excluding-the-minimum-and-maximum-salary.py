from typing import List

class Solution:
    def average(self, salary: List[int]) -> float:
        # Find minimum and maximum salary
        min_salary = min(salary)
        max_salary = max(salary)
        
        # Calculate the sum of all salaries except min and max
        total_sum = sum(salary) - min_salary - max_salary
        
        # Calculate the number of elements excluding min and max
        count = len(salary) - 2
        
        # Return the average
        return total_sum / count
