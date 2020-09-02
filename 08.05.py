class Solution:
    def multiply(self, A: int, B: int) -> int:
        def mul(small, big):
            if small == 1:
                return big
            s = small >> 1
            half = mul(s, big)
            if small & 1 == 1:
                return big + half + half
            else:
                return half + half

        if A > B:
            A, B = B, A
        return mul(A, B)


if __name__ == "__main__":
    s = Solution()
    print()
