class Node:

    def __init__(self, val):

        self.val = val
        self.next = None # 這個next是一個pointer，用來指向後來放的Node


class MyLinked:

    def __init__(self, head=None):

        # head 預設是None，後來檢測是否有node，再把node掛上去，注意這邊的head，要掛的是一個node，而不是一個value
        self.head = head
        self.end = head

    def add(self, val):
        # time complexity O(1)
        if self.head == None:
            self.head = Node(val)  # 記得linked list要掛上去的是一個Node
            self.end = self.head
        else:
            self.end.next = Node(val)
            self.end = self.end.next

    def search(self, val):
        # time complexity O(n)
        if self.head == None:
            return None

        curr_node = self.head
        while True:
            if curr_node == None:
                return None
            if curr_node.val == val:
                return curr_node.val
            curr_node = curr_node.next

    def remove(self, val):
        # time complexity O(n)
        curr_node = self.head
        pre_node = None

        while True:

            if curr_node == None:
                return None

            if curr_node.val == val:
                if pre_node == None:
                    # 表示在第一個head就找到val
                    self.head = curr_node.next
                else:
                    pre_node.next = curr_node.next

                break

            pre_node = curr_node
            curr_node = curr_node.next


if __name__ == "__main__":

    linked_ls = MyLinked(Node(1))

    linked_ls.add(9)

    linked_ls.add(11)
    linked_ls.add(2)
    linked_ls.add(98)
    linked_ls.add(35)

    val = linked_ls.search(98)

    linked_ls.remove(2)
    linked_ls.remove(9)
    linked_ls.remove(35)

