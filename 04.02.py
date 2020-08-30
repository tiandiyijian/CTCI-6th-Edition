from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def build(low, high):
            if low == high:
                return TreeNode(nums[low])
            if low > high:
                return None
            mid = (high + low) // 2
            root = TreeNode(nums[mid])
            root.left = build(low, mid - 1)
            root.right = build(mid + 1, high)
            return root

        return build(0, len(nums) - 1)


if __name__ == "__main__":
    s = Solution()
    print(s.sortedArrayToBST([1,2,3]))