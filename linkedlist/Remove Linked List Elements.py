# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int):
        ptr = head
        pptr = None
        
        while ptr:
            if ptr.val == val:    
                if pptr == None:
                    head = ptr.next
                else:
                    pptr.next = ptr.next
                    
            else:
                pptr = ptr
            ptr = ptr.next
        
        return head
        