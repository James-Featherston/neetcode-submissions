# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        lead = head.next
        trail = head
        head.next = None
        while lead:
            temp = lead.next
            lead.next = trail
            trail = lead
            lead = temp
        return trail
            
        