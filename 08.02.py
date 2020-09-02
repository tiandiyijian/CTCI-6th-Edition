class Solution:
    def pathWithObstacles(self, obstacleGrid: List[List[int]]) -> List[List[int]]:
        failed_points = set()

        def dfs(x, y, path):
            if x < 0 or y < 0 or obstacleGrid[x][y] or (x, y) in failed_points:
                return False
            if x == 0 and y == 0 or dfs(x - 1, y, path) or dfs(x, y - 1, path):
                path.append([x, y])
                return True
            failed_points.add((x, y))

        path = []
        if dfs(len(obstacleGrid) - 1, len(obstacleGrid[0]) - 1, path):
            return path
        return []


if __name__ == "__main__":
    s = Solution()
    print()
