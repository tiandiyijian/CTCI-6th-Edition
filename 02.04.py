# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head:
            return head
        rhead = head
        while head.next:
            if head.next.val < x:
                tmp = head.next
                head.next = tmp.next
                tmp.next = rhead
                rhead = tmp
            else:
                head = head.next
        return rhead


if __name__ == "__main__":
    s = Solution()
    print()
