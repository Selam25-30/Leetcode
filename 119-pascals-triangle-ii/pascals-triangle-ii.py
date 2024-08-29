from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]  # The first element is always 1
        for i in range(1, rowIndex + 1):
            row.append(row[i - 1] * (rowIndex - i + 1) // i)
        return row
