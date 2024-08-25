from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # Initialize the result as an empty list
        triangle = []

        # Iterate over the number of rows
        for i in range(numRows):
            # Start each row with a 1
            row = [1] * (i + 1)

            # Fill in the values between the first and last elements
            for j in range(1, i):
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]

            # Append the row to the triangle
            triangle.append(row)

        return triangle
