import collections


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        count = 0
        sum_count = collections.defaultdict(int)
        sum_count[0] = 1

        def dfs(node, current_sum):
            if not node:
                return
            
            nonlocal count, sum_count, sum
            current_sum += node.val
            count += sum_count[current_sum - sum]

            sum_count[current_sum] += 1
            dfs(node.left, current_sum)
            dfs(node.right, current_sum)
            sum_count[current_sum] -= 1

        dfs(root, 0)
        return count
