# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        val_left = self.maxDepth(root.left)
        val_right = self.maxDepth(root.right)
        val = max(val_left, val_right)
        return val + 1
