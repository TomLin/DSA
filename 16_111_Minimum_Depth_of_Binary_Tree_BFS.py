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

        ls = []
        ls.append(root)
        depth = 0

        while len(ls) > 0:

            n = len(ls)
            depth += 1

            for _ in range(n):

                node = ls.pop(0)

                if not node:
                    continue
                elif not node.left and not node.right:
                    return depth
                else:
                    ls.append(node.left)
                    ls.append(node.right)