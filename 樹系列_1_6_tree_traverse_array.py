"""
我們也可以改變視角，利用array的方式，來表示一個tree. 所以一個[1,2,3,4,5,6,7]的陣列，就是表示下面這顆樹：
1
2 3
4 5 6 7

因此下面就來試看看，不build一個tree，而是用list traverse的方式，進行pre-order/in-order/post-order的作法。

這邊將利用parent and child node index的特性來建立tree，如下說明。

針對一個list，裡面的元素：
如果parent node的index是i，那麼它的left child node就是2i+1，而right child node就是2i+2。
反過來說，如果知道一個child node的index是i，那它的parent node index就是floor((i-1)/2)。

REF: https://www.vitoshacademy.com/python-build-a-binary-tree-list-in-python/
"""

class MyTree:

    def __init__(self, nums):

        self.nums = nums
        self.nums_len = len(nums)

    def left_preorder(self, i):
        """DFS left的traverse法，記住喔！preorder的話，是一看到就先列印"""
        if i >= self.nums_len:
            return
        else:

            # 求下一個左右子節點index
            i_left = 2*i + 1
            i_right = 2*i+2

            print(str(self.nums[i]) + " -> ", end="")
            self.left_preorder(i_left)
            self.left_preorder(i_right)

    def right_preorder(self, i):
        """DFS right的traverse法，基本上就是DFS left的小調整"""
        if i >= self.nums_len:
            return
        else:
            i_left = 2*i + 1
            i_right = 2*i+2

            print(str(self.nums[i]) + " -> ", end="")

            # 改成先從右邊走下去，回頭再往左邊探一探路，看是不是能夠在下面往右走
            self.right_preorder(i_right)
            self.right_preorder(i_left)


if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7]
    b_tree = MyTree(nums)
    b_tree.left_preorder(i=0)
    print("\nEnd of left pre-order")
    b_tree.right_preorder(i=0)
    print("\nEnd of right pre-order")

