# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        if not l1 or not l2:
            return None
        if not l1:
            return l2
        if not l2:
            return l1
        s = l1.val + l2.val + carry
        res = ListNode(s % 10)
        final = res
        carry = s // 10
        l2 = l2.next
        l1 = l1.next
        while l1 or l2:
            if not l2:
                s = l1.val + carry
                carry = s // 10
                l1 = l1.next
            elif not l1:
                s = l2.val + carry
                carry = s // 10
                l2 = l2.next
            else:
                s = l1.val + l2.val + carry
                carry = s // 10
                l2 = l2.next
                l1 = l1.next
            res.next = ListNode(s % 10)
            res = res.next
        if carry == 1:
            res.next = ListNode(1)
        return final
        