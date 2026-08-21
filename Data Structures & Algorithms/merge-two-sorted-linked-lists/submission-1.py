# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        res = None
        if not list1 and not list2:
            return None
        if not list2:
            res = ListNode(list1.val)
            list1 = list1.next
        elif not list1:
            res = ListNode(list2.val)
            list2 = list2.next
        elif list1.val < list2.val:
            res = ListNode(list1.val)
            list1 = list1.next
        else:
            res = ListNode(list2.val)
            list2 = list2.next
        final = res
        while list1 or list2:
            if not list2:
                res.next = ListNode(list1.val)
                list1 = list1.next
            elif not list1:
                res.next = ListNode(list2.val)
                list2 = list2.next
            elif list1.val < list2.val:
                res.next = ListNode(list1.val)
                list1 = list1.next
            else:
                res.next = ListNode(list2.val)
                list2 = list2.next
            res = res.next
            

        return final
        