class Solution:
    def insertBits(self, N: int, M: int, i: int, j: int) -> int:
        all_ones = (1 << 32) -1
        left = all_ones << (j + 1)
        right = ((1 << i) - 1)
        mask = left | right
        print(bin(mask))
        
        N = N & mask
        M = M << i
        print(bin(N), bin(M))
        return M | N



if __name__ == "__main__":
    s = Solution()
    print(s.insertBits(1024, 19, 2, 6))