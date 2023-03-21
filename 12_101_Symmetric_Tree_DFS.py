# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:

        if root is None:
            return True

        left = root.left
        right = root.right

        return self.compareTree(left, right)


    def compareTree(self, l, r):

        if not l and not r:
            return True
        elif not l or not r:
            return False
        elif l.val != r.val:
            return False
        else:
            return self.compareTree(l.right, r.left) and self.compareTree(l.left, r.right)