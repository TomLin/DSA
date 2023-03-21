# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        """
        Ref: (NeetCode) https://youtu.be/RF_M9tX4Eag
        1) 這邊有一個技巧，就是在list前面多加一個dummy的node，這樣可以處理下面兩種麻煩的edge case:
            a) common case會是，原本的tail，會反轉接回之前的head，
            如果反轉的left，是在第一個，那麼它原本的tail，就會接到前面的None，爆錯(例外情況)
            b) common case會是回傳固定的head，但是如果反轉的left，是在第一個，那麼它的tail，就會變成新的head(例外情況)
        """
        if not head:
            return None


        dummy = ListNode(-1)
        dummy.next = head

        pre, cur = dummy, dummy.next

        # 從head開始，要跳left-1次，到left node上頭
        for i in range(left-1):
            pre = cur
            cur = cur.next

        # 反轉前的node，等一下用來接反轉後的linked list
        node_in_front = pre
        pre = None
        # 進行反轉，需要反轉right-left+1次，從left node到right node(inclusive)，都需要反轉
        for i in range(right-left+1):
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        node_in_front.next.next = cur
        node_in_front.next = pre
        return dummy.next





