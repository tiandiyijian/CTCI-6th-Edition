class Solution:
    def reverseBits(self, num: int) -> int:
        pre = current = 0
        ans = 1
        while num:
            val = num & 1
            if val == 1:
                current += 1
            else:
                ans = max(ans, current + pre + 1)
                pre = 0 if num & 2 == 0 else current
                current = 0
            num >>= 1
        ans = max(ans, current + pre + 1)
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
