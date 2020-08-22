class Solution:
    def isUnique(self, astr: str) -> bool:
        if len(astr) > 26:
            return False
        mask = 0
        for c in astr:
            tmp = ord(c) - ord('a')
            tmp = 1 << tmp
            if mask & tmp > 0:
                return False
            else:
                mask |= tmp
        return True


if __name__ == "__main__":
    s = Solution()
    print(s.isUnique('leetcode'))
