# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
心得：
1) 不管切割多少個linked list，都需要保留行個list的頭，這樣之後才能找得到那個list(可以使用tmp node來作入口)。
2) 在linked list當中，想要對分切，可以使用快慢指針的技巧，這個技巧，也常用在其它方面，例如偵測是否有cycle linked list。
3) 創造dummy node在一開始的空linked list，這會是常見的技巧，可以避免一些edge case，例如要調整head的時候，發現head是none，那就不好處理了。
"""


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head or not head.next:
            return head

        # 在進行split時，要保留的左邊子list的頭
        left = head

        # divide()函數，回傳右邊子list頭的再前一個node
        right = self.divide(head)
        tmp = right.next
        right.next = None
        right = tmp

        # recursively split the linked list
        left = self.sortList(left)
        right = self.sortList(right)

        return self.merge(left, right)

    def divide(self, head):
        slow, fast = head, head.next

        while fast and fast.next:
            fast = fast.next.next  # 快指針，每次都以二倍速走
            slow = slow.next
        return slow

    def merge(self, list1, list2):
        cur = ListNode(-1)  # fake node

        # 保留這個linked list進入的端口
        head = cur

        while list1 and list2:
            if list1.val <= list2.val:
                cur.next = list1
                list1 = list1.next # update 它的指針
            else:
                cur.next = list2
                list2 = list2.next
            cur = cur.next

        if list1:
            cur.next = list1
        if list2:
            cur.next = list2

        return head.next