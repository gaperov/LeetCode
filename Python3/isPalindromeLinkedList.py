# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def find_second_half(head):
            slow = head
            fast = head
            while fast and fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        
        def reverse_second_half(slow):
            prev, cur = None, slow.next
            while cur:
                temp = cur.next
                cur.next = prev

                prev = cur
                cur = temp
            return prev
        
        def is_palindrome(head, prev):
            h1 = head
            h2 = prev
            while h1 and h2:
                if h1.val != h2.val:
                    return False
                h1 = h1.next
                h2 = h2.next
            return True
        
        prehead_second_part = find_second_half(head)
        back_head = reverse_second_half(prehead_second_part)
        return is_palindrome(head, back_head)
