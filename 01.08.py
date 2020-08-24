from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        first_row_zero = first_col_zero = False
        for i in range(m):
            if matrix[i][0] == 0:
                first_col_zero = True
                break
        for i in range(n):
            if matrix[0][i] == 0:
                first_row_zero = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                matrix[i][:] = [0] * n

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0

        if first_row_zero:
            matrix[0][:] = [0] * n

        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0


if __name__ == "__main__":
    s = Solution()
    m = [[1,1,1],[1,0,1],[1,1,1]]
    s.setZeroes(m)
    print(m)
