# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
心得：
這邊原本我以為會遇到一個問題，是左右子節點都會回傳符合條件的子樹，但是題目剛好設計成binary search tree，所以一個值，應該只會出現在一個地方
"""

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        if not root:
            return None
        elif root.val == val:
            return root
        else:
            root1 = self.searchBST(root.left, val)
            root2 = self.searchBST(root.right, val)

            if not root1 and not root2:
                return None
            elif not root1:
                return root2
            else:
                return root1

