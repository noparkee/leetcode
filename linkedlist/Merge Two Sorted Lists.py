# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode):
        if l1 == None and l2 == None:
            return None
        elif l1 and l2 == None:
            return l1
        elif l1 == None and l2:
            return l2
        
        
        if l1.val < l2.val:
            head = l1
            l1 = l1.next
        else:
            head = l2
            l2 = l2.next
            
        ptr = head
            
        while l1 and l2:
            if l1.val < l2.val:
                ptr.next = l1
                ptr = ptr.next
                l1 = l1.next
            else:
                ptr.next = l2
                ptr = ptr.next
                l2 = l2.next
        
        if l1:
            ptr.next = l1
        else:
            ptr.next = l2
        
        return head
            