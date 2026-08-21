# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        target = length - n
        prev = None
        curr = head
        idx = 0
        while idx < target:
            idx += 1
            prev = curr
            curr = curr.next
        
        if prev != None:
            prev.next = curr.next
        else:
            head = head.next
        return head
        