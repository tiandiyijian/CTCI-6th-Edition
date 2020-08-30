# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        ans = None
        p_flag = False

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            nonlocal p_flag, ans
            if p_flag and ans is None:
                ans = node
                return
            if node is p:
                p_flag = True
            
            inorder(node.right)

        inorder(root)
        return ans

    def inorderSuccessor(self, root: TreeNode, p: TreeNode) -> TreeNode:
        if p.right:
            node = p.right
            while node.left:
                node = node.left
            return node
        tmp = root
        ans = None
        while tmp is not p:
            if tmp.val < p.val:
                tmp = tmp.right
            elif tmp.val > p.val:
                tmp = tmp.left
                ans = tmp
        return ans