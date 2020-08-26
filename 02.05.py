# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(-1)
        prev = dummy
        carry = 0
        while l1 or l2 or carry > 0:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            tmp_sum = v1 + v2 + carry
            carry = tmp_sum // 10
            prev.next = ListNode(tmp_sum % 10)
            prev = prev.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next


if __name__ == "__main__":
    s = Solution()
    print()
