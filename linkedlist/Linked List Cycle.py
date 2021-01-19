# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode):
        pre = head
        pren = head
        
        while pre!=None and pren!=None and pren.next!=None:
            pre = pre.next
            pren = pren.next.next
            
            
            if pre == pren:
                return True
        
        return False
        
# pre는 한 개 씩, pren은 두 개 씩 만약 cycle이 있으면 언젠가는 만나게 됨.