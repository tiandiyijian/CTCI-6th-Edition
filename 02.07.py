# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        ha, hb = headA, headB
        la = lb = 0
        while ha or hb:
            if ha:
                la += 1
                ha = ha.next
            if hb:
                lb += 1
                hb = hb.next

        if la > lb:
            for _ in range(la - lb):
                headA = headA.next
        elif la < lb:
            for _ in range(lb - la):
                headB = headB.next

        while headA and headB:
            if headA == headB:
                return headA
            else:
                headA = headA.next
                headB = headB.next

        return None


if __name__ == "__main__":
    s = Solution()
    print()
