# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def BSTSequences(self, root: TreeNode) -> List[List[int]]:
        def wave_two_list(a, b):
            if not a:
                return [b]
            if not b:
                return [a]
            ans = []
            def build(i, j, seq):
                if i < len(a):
                    build(i+1, j, seq + [a[i]])
                if j < len(b):
                    build(i, j+1, seq + [b[j]])
                if i == len(a) and j == len(b):
                    ans.append(seq)
            build(0, 0, [])
            return ans
        
        def wave(la, lb, prefix):
            ans = []
            for a in la:
                for b in lb:
                    tmp = wave_two_list(a, b)
                    for t in tmp:
                        ans.append([prefix] + t)
            return ans

        if not root:
            return [[]]
        
        prefix = root.val
        left = self.BSTSequences(root.left)
        right = self.BSTSequences(root.right)

        return wave(left, right, prefix)