# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        採用pre-order的型式，進行「兩棵樹」的判斷。
        它的時間複雜度是O(min(M,N))
        '''

        if (p is None) and (q is None):
            return True

        elif (p is None) and (q is not None):
            return False

        elif (p is not None) and (q is None):
            return False

        elif p.val != q.val:
            return False

        else:
            # 因為在class下面，所以呼叫自己時，記得要再加上self.fun()，要不然會噴錯
            # 在程式中的and，指的是兩邊的判斷式都要成立，才會return True，如果兩邊判斷式都是False，那麼它還是會回傳False，不像數學的負負得正
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class Solution_2:

    def isSameTree(self, p, q):
        '''
        下面的寫法，比較簡潔，直接用not p or not q，來包含任一個節點為None的狀況。
        '''

        if not p and not q:
            return True

        elif not p or not q:
            return False

        elif p.val != q.val:
            return False

        else:
            # 因為在class下面，所以呼叫自己時，記得要再加上self.fun()，要不然會噴錯
            # 在程式中的and，指的是兩邊的判斷式都要成立，才會return True，如果兩邊判斷式都是False，那麼它還是會回傳False，不像數學的負負得正
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
