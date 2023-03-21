# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0
        elif not root.left and not root.right:
            return 1
        elif root.left and root.right:
            val_left = self.minDepth(root.left)
            val_right = self.minDepth(root.right)
            val = min(val_left, val_right)
        elif root.left:
            val = self.minDepth(root.left)
        elif root.right:
            val = self.minDepth(root.right)

        return val + 1
