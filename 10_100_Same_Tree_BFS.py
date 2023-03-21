# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:

        ls_p = []
        ls_q = []

        ls_p.append(p)
        ls_q.append(q)

        while True:

            if len(ls_p) == 0 and len(ls_q) == 0:
                return True

            p = ls_p.pop(0)
            q = ls_q.pop(0)

            if not p and not q:
                continue
            elif not p or not q:
                return False
            elif p.val != q.val:
                return False
            else:
                ls_p.append(p.left)
                ls_p.append(p.right)

                ls_q.append(q.left)
                ls_q.append(q.right)