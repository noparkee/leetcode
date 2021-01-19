# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode):
        a = headA
        b = headB
        acnt = 0
        bcnt = 0
        while a != None:
            a = a.next
            acnt += 1
        while b != None:
            b = b.next
            bcnt += 1
            
        cnt = acnt - bcnt
        a = headA
        b = headB
        if cnt < 0:
            cnt *= -1
            while cnt > 0:
                b = b.next
                cnt -=1
        else:
            while cnt > 0:
                a = a.next
                cnt -= 1
        
        while a != b:
            a = a.next
            b = b.next
            
        if a==b:
            return a
        