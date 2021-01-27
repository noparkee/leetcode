# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode):
        c = 0
        
        head = ListNode(0)
        ptr = head
        
        
        while l1 and l2:
            a = l1.val
            b = l2.val
            l1 = l1.next
            l2 = l2.next
            s = a + b + ptr.val
            
            c = s//10
            s = s%10
            
            ptr.val = s
            if l1 == None and l2 == None and c==0:
                break
            ptr.next = ListNode(c)
            
            ptr = ptr.next

        
        while l1:
            a = l1.val
            l1 = l1.next
            s = a + ptr.val
            c = s//10
            s = s%10
            ptr.val = s
            if l1 == None and c==0:
                break
            ptr.next = ListNode(c)
            ptr = ptr.next
            
        
        while l2:
            a = l2.val
            l2 = l2.next
            s = a + ptr.val
            c = s//10
            s = s%10
            ptr.val = s
            if l2 == None and c==0:
                break
            ptr.next = ListNode(c)
            ptr = ptr.next
                    
        return head
        