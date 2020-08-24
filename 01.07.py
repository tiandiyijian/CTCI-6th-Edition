from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)

        def rotate_point(layer, i):
            tmp = matrix[layer][i]
            matrix[layer][i] = matrix[n - 1 - i][layer]
            matrix[n - 1 - i][layer] = matrix[n - 1 - layer][n - 1 - i]
            matrix[n - 1 - layer][n - 1 - i] = matrix[i][n - 1 - layer]
            matrix[i][n - 1 - layer] = tmp

        for layer in range((n - 1) // 2 + 1):
            for i in range(n - layer * 2 - 1):
                rotate_point(layer, layer + i)
        # return matrix


if __name__ == "__main__":
    s = Solution()
    m = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
    s.rotate(m)
    print(m)
