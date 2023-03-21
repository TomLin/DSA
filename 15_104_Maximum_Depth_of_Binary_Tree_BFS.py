# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from typing import Optional

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        depth = 0
        ls = []
        ls.append(root)

        while len(ls) > 0:

            # 這裡的n就是用就判斷該層的長度，這樣才知道什麼時候結束，進入下一層
            n = len(ls)
            for _ in range(n):

                root = ls.pop(0)

                if not root:
                    continue

                ls.append(root.left)
                ls.append(root.right)

            depth += 1

        return depth - 1