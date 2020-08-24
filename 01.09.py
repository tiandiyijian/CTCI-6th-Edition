class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        return len(s1) == len(s2) and (s1 + s1).find(s2) >= 0


if __name__ == "__main__":
    s = Solution()
    print()
