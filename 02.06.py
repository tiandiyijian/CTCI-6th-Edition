# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = fast = head
        count = 0  # 长度的一半
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            count += 1
        if fast:
            slow = slow.next

        def helper(node, count):
            nonlocal slow
            if count == 1:
                tmp = slow.val
                slow = slow.next
                return node.val == tmp
            back = helper(node.next, count - 1)
            tmp = slow.val
            slow = slow.next
            return back and node.val == tmp

        return helper(head, count)


if __name__ == "__main__":
    s = Solution()
    print()
