class Solution:
    def waysToStep(self, n: int) -> int:
        if n < 3:
            return n
        if n == 3:
            return 4

        n1 = 1
        n2 = 2
        n3 = 4

        for i in range(4, n + 1):
            n1, n2, n3 = n2, n3, (n1 + n2 + n3) % 1000000007
        return n3 % 1000000007


if __name__ == "__main__":
    s = Solution()
    print()
