class Solution:
    def printBin(self, num: float) -> str:
        if num > 1 or num < 0:
            return 'ERROR'
        ans = "0."
        frac = 0.5
        while num > 0:
            if len(ans) > 32:
                return 'ERROR'
            if num >= frac:
                ans += '1'
                num -= frac
            else:
                ans += '0'
            frac /= 2
        return ans


if __name__ == "__main__":
    s = Solution()
    print()
