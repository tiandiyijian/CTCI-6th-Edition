class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        if len(s1) != len(s2):
            return False
        mask1 = mask2 = 0
        for c1, c2 in zip(s1, s2):
            mask1 |= (1 << (ord(c1) - ord('a')))
            mask2 |= (1 << (ord(c2) - ord('a')))
        return mask1 == mask2


if __name__ == "__main__":
    s = Solution()
    print(s.CheckPermutation('abc', 'bca'))
