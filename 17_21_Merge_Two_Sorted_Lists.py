# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
- 在操作linked list上頭，一定要把head保留住，每一次要提取資料，都只能從head，從新開始往下一個個節點找值。
- 這是linked list的特色，在寫leetcode的時候，一定要注意。
- 另一個常用的，就是用current node，來指涉現在要進行處理的node。
"""

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

        cur = ListNode(-1)  # fake node
        # 這邊保留home node，這是這個linked list的入口
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