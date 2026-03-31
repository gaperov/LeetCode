# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        len_a = 0
        cur = headA
        while cur:
            len_a += 1
            cur = cur.next

        len_b = 0
        cur = headB
        while cur:
            len_b += 1
            cur = cur.next

        if len_a > len_b:
            n = len_a - len_b
            longer = headA
            shorter = headB
        else:
            n = len_b - len_a
            longer = headB
            shorter = headA
        
        while n:
            longer = longer.next
            n -= 1
        
        while longer:
            if longer == shorter:
                return longer
            longer = longer.next
            shorter = shorter.next
