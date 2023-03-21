class Node:

    def __init__(self, val):

        self.val = val
        self.next = None

class MinStack:

    def __init__(self):

        self.stack_head = None
        self.min_stack_head = None

    def push(self, val: int) -> None:

        # Corner case: 當第一個值時
        if self.stack_head is None:
            self.stack_head = Node(val)
            self.min_stack_head = Node(val)

        # Linked List不用擔心空間的問題
        # 這邊，我們的作法，是把linked list的head，都當作stack上的top
        # 每次多加一個node，就是在linked list的head上做更新，從head，再往左加一個node上去的作法
        else:
            new_head = Node(val)
            new_head.next = self.stack_head
            self.stack_head = new_head

            # 取代新的min_val
            if val < self.min_stack_head.val:
                new_min_head = Node(val)
            else:
                new_min_head = Node(self.min_stack_head.val)

            # 再將這個head加入到min_stack裡面
            new_min_head.next = self.min_stack_head
            self.min_stack_head = new_min_head

    def pop(self) -> None:

        # Corner case: 當都沒有值時
        if self.stack_head is None:
            return None

        # 這邊，我們的作法，是從head，開始，一個個pop出值來
        else:
            val = self.stack_head.val
            self.stack_head = self.stack_head.next
            self.min_stack_head = self.min_stack_head.next
            return val

    def top(self) -> int:

        # Corner case: 當都沒有值時
        if self.stack_head is None:
            return None

        else:
            val = self.stack_head.val
            return val

    def getMin(self) -> int:

        # Corner case: 當都沒有值時
        if self.stack_head is None:
            return None

        else:
            min_val = self.min_stack_head.val
            return min_val
