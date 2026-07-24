from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        total = 0

        for i in range(n):
            # Primary diagonal
            total += mat[i][i]

            # Secondary diagonal (avoid double-counting the center)
            if i != n - 1 - i:
                total += mat[i][n - 1 - i]

        return total