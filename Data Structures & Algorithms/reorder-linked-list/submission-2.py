# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        temp = head
        size = 1
        while temp:
            size += 1
            temp = temp.next
        mid = size // 2
        if size <= 2:
            return
        
        temp = head
        for i in range(mid - 1):
            temp = temp.next
        trail = temp
        temp = temp.next
        trail.next = None

        trail = temp
        lead = temp.next

        while lead:
            temp = lead.next
            lead.next = trail
            trail = lead
            lead = temp
        res = head
        r = trail
        l = head.next

        for idx in range(1, size - 1):
            if idx % 2 == 1:
                temp = r
                r = r.next
            else:
                temp = l
                l = l.next
            res.next = temp
            res = res.next
        res.next = None
        