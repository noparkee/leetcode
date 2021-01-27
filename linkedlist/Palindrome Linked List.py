# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode):
        if head == None or head.next == None:
            return True

        ptr = head
        a = []
        b = []
        while ptr:    
            a.append(ptr.val)
            ptr = ptr.next
        
        if len(a) % 2 != 0:
            del a[len(a)//2]
            
        for i in range(len(a)//2):
            b.append(a.pop())
            
        if a==b:
            return True
        else:
            return False
    