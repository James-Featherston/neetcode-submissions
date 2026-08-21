# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        curr = head.val

        while head:
            if head.val < curr:
                return True
            curr = head.val
            head = head.next
        return False        