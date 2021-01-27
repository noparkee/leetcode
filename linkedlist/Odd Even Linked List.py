# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: ListNode):            
        if head == None:
            return None
        elif head.next == None:
            return head
        else:
            temp = head.next
        
        ptr = head
        pptr = temp
        
        while ptr.next and pptr.next:
            ptr.next = pptr.next
            if ptr != None:
                ptr = ptr.next
            pptr.next = ptr.next
            if pptr != None:
                pptr = pptr.next
            
        
        ptr.next = temp
            
        return head
        