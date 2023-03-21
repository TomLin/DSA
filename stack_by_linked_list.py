"""
不同於使用array的操作，如果使用linked list來建構stack，
我們不需要擔心長度空間會不夠，linked list可以彈性一直增加node。
"""

class Node:

    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MyStack:

    def __init__(self, arr):
        self.arr = arr
        self.node_top = None

    def build_stack(self):
        for i in range(len(self.arr)):
            self.push(self.arr[i])

    def push(self, val):

        if self.node_top is None:
            node = Node(val)
            self.node_top = node
        else:
            node = Node(val)
            node.next = self.node_top  # 記得stack是LIFO
            self.node_top = node

    def pop(self):

        if self.node_top is None:
            return None

        else:
            node = self.node_top
            self.node_top = self.node_top.next
            return node.val


if __name__ == "__main__":

    arr = [1,2,3,4,5]
    stack = MyStack(arr)
    stack.build_stack()

    stack.push(6)
    val = stack.pop()
    val = stack.pop()
    val = stack.pop()
    val = stack.pop()
    val = stack.pop()
    val = stack.pop()
    val = stack.pop()


