class Solution:
    def compressString(self, S: str) -> str:
        new_S = ""
        i = 0
        while i < len(S):
            left = i
            while i < len(S) - 1 and S[i] == S[i+1]:
                i += 1
            new_S += S[i] + str(i - left + 1)
            i += 1
        return S if len(new_S) >= len(S) else new_S


if __name__ == "__main__":
    s = Solution()
    print(s.compressString("aabcccccaa"))
