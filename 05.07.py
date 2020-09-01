class Solution:
    def exchangeBits(self, num: int) -> int:
        return ((num & 0xaaaaaaaa) >> 1) | ((num & 0x55555555) << 1)


if __name__ == "__main__":
    s = Solution()
    print(s.exchangeBits(2))