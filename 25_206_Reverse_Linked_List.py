# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        我自已第一次，寫得沒有很好的code
        """
        if not head:
            return head

        pre = None
        cur = head
        cnt = 0

        while cur:
            pre = cur
            cur = cur.next
            cnt += 1

        tail = pre

        cnt -= 1
        while cnt > 0:
            cur = head
            for i in range(cnt):
                pre = cur
                cur = cur.next

            cur.next = pre
            cnt -= 1
        head.next = None
        return tail

    def second_version(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        1) 在這個版本，是使用iterative的解法
        2) 在這邊可以注意一下，當cur_node.next斷掉後，怎麼再找回它下一個node
        """
        if not head:
            return head

        pre = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt

        return pre

    def third_version(self, head: Optional[Listnode]) -> Optional[ListNode]:
        """
        1) 這個版本，是使用recursive的方法
        2) 使用head.next.next，而不使用new_head.next的原因在於，遞迴函數回傳的，是反轉過來的第一個node，
        如果用new_head.next，就是指在這個node下一個，接現在的node -> 不對的邏輯
        """

        # 處理如果input是None的情況
        if not head:
            return None

        # 這一個，是在處理最後一個node，要讓它回傳當head
        new_head = head

        while head.next:
            head.next.next = head # 將指標反轉
            new_head = self.third_version(head.next)

        return new_head

