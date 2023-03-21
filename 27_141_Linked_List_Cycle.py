# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        """
        這是比較粗暴的作法，就是先用一個hash set，把經過的node加入，
        之後每到一個node，就比較一下，這個node，有沒有在之前出現過(由此得知，是不是cycle list)
        """
        if not head:
            return False

        set_ = set()
        cur = head

        while cur:
            if cur in set_:
                return True
            else:
                set_.add(cur)
                cur = cur.next
        return False