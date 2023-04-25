"""在這個LeetCode當中，嘗試比較兩個二元樹是不是一樣的。

例如：

1
2 2
45 45
這樣才是一樣的，或是
1
2 2
4 4
這樣也是一樣的。
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
        elif self.nums[i] is None:
            return None
        else:
            curr_node.val = self.nums[i]

        curr_node.n_left = self.build_tree(Node(), 2*i+1)
        curr_node.n_right = self.build_tree(Node(), 2*i+2)

        return curr_node

    def compare(self):

        return self.left_preorder(self.root.n_left, self.root.n_right)


    def left_preorder(self, node_1, node_2):
        """DFS left的traverse法，記住喔！preorder的話，是一看到就先列印"""

        if (node_1 is None) and (node_2 is not None):
            return False
        elif (node_1 is not None) and (node_2 is None):
            return False
        elif (node_1 is None) and (node_2 is None):
            return True
        elif node_1.val != node_2.val:
            return False
        elif node_1.val == node_2.val:
            return self.left_preorder(node_1.n_left, node_2.n_left) and self.left_preorder(node_1.n_right, node_2.n_right)
        else:
            return True


if __name__ == "__main__":
    nums = [1,2,2,3,None,3,None,4,5,None,None,4,5]  # 因為是透過index來填值，所以即便是None，也要留一個位子
    b_tree = MyTree(nums)
    tree = b_tree.build_tree(curr_node=b_tree.root, i=0)
    val = b_tree.compare()
    print(val)
    print("End")