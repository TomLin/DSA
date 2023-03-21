"""
stack最重要的特點是LIFO，像是遞迴的觀念，就和stack的處理很像，
這邊要操作的是使用array的結構，來建構一個stack的物件。

基本操作：
- 類似linked list，利用idx flag，來紀錄已經儲存了幾個數值
- push 類似於add
- pop 類似於remove

"""

class MyStack:

    def __init__(self, arr):
        self.arr = arr
        self.i_top = None  # flag用來標記目前stack最上層的index

    def build_stack(self):
        self.stack = [None] * len(self.arr)
        self.stack_len = len(self.arr)

        for i in range(len(self.arr)):
            self.push(self.arr[i])

    def push(self, val):
        if self.size() == self.stack_len:
            self.expand_space()

        if self.size() == 0:
            self.i_top = 0
        else:
            self.i_top += 1

        self.stack[self.i_top] = val

    def size(self):
        if self.i_top is None:
            return 0
        else:
            return self.i_top + 1

    def expand_space(self):
        new_stack = [None] * (self.stack_len * 2)
        for i in range(self.i_top+1):
            new_stack[i] = self.stack[i]
        self.stack = new_stack

    def pop(self):
        if self.size() == 0:
            return None
        elif self.size() == 1:
            val = self.stack[self.i_top]
            self.stack[self.i_top] = None
            self.i_top = None
            return val
        else:
            val = self.stack[self.i_top]
            self.stack[self.i_top] = None
            self.i_top -= 1
            return val


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

