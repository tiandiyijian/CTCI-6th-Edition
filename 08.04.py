from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            ans = ans + [tmp + [n] for tmp in ans]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.subsets([1, 2, 3]))
