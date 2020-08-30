# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        last = float('-inf')

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False

            nonlocal last
            if node.val <= last:
                return False
            last = node.val

            if not inorder(node.right):
                return False

            return True

        return inorder(root)
