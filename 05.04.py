class Solution:
    def findClosedNumbers(self, num: int) -> List[int]:
        # larger
        # 把非拖尾的0变1，所以先找拖尾的0的个数，再找相邻的1的个数，就可以找到第一个非拖尾的0所在的位数
        c = num
        c0 = c1 = 0
        while c & 1 == 0:
            c0 += 1
            c >>= 1
        while c & 1 == 1:
            c1 += 1
            c >>= 1
        larger = num + (1 << c0) + (1 << (c1 - 1)) - 1

        # smaller
        # 把非拖尾的1变0，所以先找拖尾的1的个数，再找相邻的0的个数，就可以找到第一个非拖尾的1所在的位数
        c = num
        c0 = c1 = 0
        while c & 1 == 1:
            c1 += 1
            c >>= 1
        if c == 0:
            return [larger, -1]
        while c & 1 == 0:
            c0 += 1
            c >>= 1
        smaller = num - (1 << c1) - (1 << (c0 - 1)) + 1

        return [larger, smaller]


if __name__ == "__main__":
    s = Solution()
    print()
