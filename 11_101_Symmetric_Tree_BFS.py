# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        ls_l = []
        ls_r = []

        ls_l.append(root.left)
        ls_r.append(root.right)

        while True:

            if len(ls_l) == 0 and len(ls_r) == 0:
                return True

            l = ls_l.pop(0)
            r = ls_r.pop(0)

            if not l and not r:
                continue

            elif not l or not r:
                return False

            elif l.val != r.val:
                return False

            else:
                # 針對左節點，使用breadth first search (right) 的走法
                ls_l.append(l.right)
                ls_l.append(l.left)

                # 針對右節點，使用breadth first search (left) 的走法
                ls_r.append(r.left)
                ls_r.append(r.right)