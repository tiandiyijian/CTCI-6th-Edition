# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        def helper(node):
            if not node:
                return 0, True
            left_height, left_balanced = helper(node.left)
            if not left_balanced:
                return left_height, False
            right_height, right_balanced = helper(node.right)
            if not right_balanced:
                return right_height, False
            if abs(left_height - right_height) <= 1:
                return max(left_height, right_height) + 1, True
            else:
                return max(left_height, right_height) + 1, False

        return helper(root)[1]
