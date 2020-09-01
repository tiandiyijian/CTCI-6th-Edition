class Solution:
    def convertInteger(self, A: int, B: int) -> int:
        def rshift(val, n):
            return val >> n if val >= 0 else (val+0x100000000) >> n

        count = 0
        while A or B:
            count += (A & 1) ^ (B & 1)
            A = rshift(A, 1)
            B = rshift(B, 1)
        return count


if __name__ == "__main__":
    s = Solution()
    print()
