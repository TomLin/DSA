"""
要從一串list建構一個binary tree，因為它有點類似BFS的操作，因此可以用loop的方式去寫程式碼。
但是在這邊，我們也可以利用recursion的寫法，來試著建構這個binary tree。
1
2 3
4 5 6 7
8 9 10 11 12
....

這邊將利用parent and child node index的特性來建立tree，如下說明。

針對一個list，裡面的元素：
如果parent node的index是i，那麼它的left child node就是2i+1，而right child node就是2i+2。
反過來說，如果知道一個child node的index是i，那它的parent node index就是floor((i-1)/2)。

REF: (recursion的寫法) https://www.geeksforgeeks.org/construct-complete-binary-tree-given-array/
REF: https://www.vitoshacademy.com/python-build-a-binary-tree-list-in-python/
"""

class Node:

    def __init__(self, val=None, n_left=None, n_right=None):
        self.val = val
        self.n_left = n_left
        self.n_right = n_right


class MyTree:

    def __init__(self, nums):

        self.nums = nums
        self.nums_len = len(self.nums)
        self.root = Node()  # create an empty root node
        self.curr = self.root

    def build_tree(self, curr_node, i):

        if i >= self.nums_len:
            return None
        else:
            curr_node.val = self.nums[i]

        curr_node.n_left = self.build_tree(Node(), 2*i+1)
        curr_node.n_right = self.build_tree(Node(), 2*i+2)

        return curr_node


    def left_preorder(self, node):
        """DFS left的traverse法，記住喔！preorder的話，是一看到就先列印"""

        if node == None:
            return
        else:
            print(str(node.val) + " -> ", end="")

            self.left_preorder(node.n_left)
            # 把左邊都看完後，再探一探頭，看一下右邊，是不是有分支，可以下去接著往左走
            self.left_preorder(node.n_right)

    def left_inorder(self, node):
        """DFS left的traverse法，inorder的話，是左邊先走完後，回來時列印，再往右邊走，如果對象是個binary search tree，
        右子節點大於左子節點，那麼使用inorder的話，就會看到由小到大的排序"""

        if node == None:
            return
        else:
            self.left_inorder(node.n_left)
            print(str(node.val) + " -> ", end="")

            # 之後再往右邊探一探頭，看是不是能在往下接著向左走
            self.left_inorder(node.n_right)

    def left_postorder(self, node):
        """DFS left的traverse法，postorder的話，可以想像成是兩邊子結點都已經走完後，這個母節點才會印出來"""

        if node == None:
            return
        else:
            self.left_postorder(node.n_left)
            self.left_postorder(node.n_right)
            print(str(node.val) + " -> ", end="")


if __name__ == "__main__":

    nums = [1,2,3,4,5,6,7]
    b_tree = MyTree(nums)
    b_tree.build_tree(curr_node=b_tree.curr, i=0)
    print("End")
    b_tree.left_preorder(b_tree.root)
    print("\nEnd of left pre-order")
    b_tree.left_inorder(b_tree.root)
    print("\nEnd of left in-order")
    b_tree.left_postorder(b_tree.root)
    print("\nEnd of left post-order")