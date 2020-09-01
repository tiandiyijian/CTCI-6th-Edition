class Solution:
    def drawLine(self, length: int, w: int, x1: int, x2: int, y: int) -> List[int]:
        ans = [0] * length
        low = (y * w + x1) // 32
        high = (y * w + x2) // 32

        for i in range(low, high+1):
            ans[i] = -1

        if x1 % 32 != 0:
            ans[low] += 1 << (32 - x1 % 32)
        ans[high] -= (1 << (32 - x2 % 32 - 1)) - 1

        return ans
