"""
要從一串list建構一個binary tree，因為它有點類似BFS的操作，因此可以用loop的方式去寫程式碼。
1
2 3
4 5 6 7
8 9 10 11 12
....

下面就嘗試用loop的方式，建構一個binary tree，因為linked list沒有index的概念，因此我們預先建構一個list，來存放node.
並且利用parent and child node index的特性來建立tree，如下說明。

針對一個list，裡面的元素：
如果parent node的index是i，那麼它的left child node就是2i+1，而right child node就是2i+2。
反過來說，如果知道一個child node的index是i，那它的parent node index就是floor((i-1)/2)。

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

    def build_tree(self):

        self.root = None
        nodes_ls = []

        # 先將每個node的值填入list
        for i in range(self.nums_len):
            nodes_ls.append(Node(self.nums[i]))

        self.root = nodes_ls[0]

        # 開始依序為每個節點的左右子節點建立link
        for i in range(self.nums_len):
            left_idx = 2*i + 1
            right_idx = 2*i + 2

            curr_node = nodes_ls[i]
            if left_idx < self.nums_len:
                curr_node.n_left = nodes_ls[left_idx]
            if right_idx < self.nums_len:
                curr_node.n_right = nodes_ls[right_idx]



if __name__ == "__main__":

    nums = [1,2,3,4]
    b_tree = MyTree(nums)
    b_tree.build_tree()
    print("End")



