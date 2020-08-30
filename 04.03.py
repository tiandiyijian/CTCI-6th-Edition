import collections
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# Definition for singly-linked list.


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def listOfDepth(self, tree: TreeNode) -> List[ListNode]:
        ans = []
        q = collections.deque([tree])
        while q:
            size = len(q)
            head = dummy = ListNode(-1)
            for _ in range(size):
                tmp = q.popleft()
                head.next = ListNode(tmp.val)
                head = head.next
                if tmp.left:
                    q.append(tmp.left)
                if tmp.right:
                    q.append(tmp.right)
            ans.append(dummy.next)
        return ans
