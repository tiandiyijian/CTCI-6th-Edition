import collections
from typing import List


class Solution:
    def findWhetherExistsPath(self, n: int, graph: List[List[int]], start: int, target: int) -> bool:
        q = collections.deque()
        q.append(start)
        visited = [0] * n
        visited[start] = True

        neighbor = collections.defaultdict(list)
        for a, b in graph:
            neighbor[a].append(b)

        while q:
            tmp = q.popleft()
            if tmp == target:
                return True
            for n in neighbor[tmp]:
                if visited[n] == 0:
                    visited[n] = 1
                    q.append(n)

        return False


if __name__ == "__main__":
    s = Solution()
    print()
