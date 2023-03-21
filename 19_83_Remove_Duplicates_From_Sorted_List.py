# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head and head.next:
            pre = head
            cur = head.next
        else:
            return head

        while cur:

            if pre.val == cur.val:
                pre.next = cur.next
                cur = pre.next
            else:
                pre = cur
                cur = cur.next

        return head