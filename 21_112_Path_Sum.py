# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
1. 把它想成一個pre-order的問題。
2. 仔細觀察，可以看到這個函數只接受一個node，還有一個targetSum。
3. 所以不需要用原本的溝想，先把一個個node的value存成一個值，再和這個targetSum相減，
而是直接把targetSum在每一個節點就先減掉了，再往下傳遞。
4. 因為樹所長成的眾多路徑，怎麼樣把不符合條件的路徑，刪除掉，而只回傳符合條件的路徑，
可以觀察一下，下面是怎麼寫的(在最後一個return裡面，把答案一層層地回傳上去)。
5. 但是同樣要寫一下，符合狀況的條件(在中間的那一個if條件裡面)。
"""

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        targetSum = targetSum - root.val

        if (not root.left) and (not root.right) and targetSum == 0:
            return True

        else:
            return self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum)
