"""
在queue的設計中，常常會搭配上循環的用法(circular queue)，也就是queued的尾巴，接上它的頭。
通常這個實作，是會使用array實現(因為array的長度有限度，需要把空下來的空間再利用)，而不需要使用linked list。

基本操作：
- enqueue/offer: 就是add
- dequeue/poll: 就是remove

"""

class MyQueue:

    def __init__(self, nums):
        self.nums = nums
        self.i_front = None
        self.i_end = None

    def build_queue(self):
        self.queue = [None] * len(self.nums)
        self.queue_len = len(self.nums)

        for i in range(len(self.nums)):
            self.enqueue(self.nums[i])

    def enqueue(self, val):

        if self.size() == self.queue_len:
            self.expand_queue()

        if self.size() == 0:
            self.i_front = 0
            self.i_end = 0
        else:
            self.i_end = (self.i_end + 1) % self.queue_len

        self.queue[self.i_end] = val

    def size(self):
        if self.i_front == None and self.i_end == None:
            return 0
        elif self.i_end >= self.i_front:
            return self.i_end - self.i_front + 1
        elif self.i_end < self.i_front:
            return self.queue_len - (self.i_front - self.i_end - 1)

    def expand_queue(self):
        new_queue = [None] * (self.queue_len * 2)

        i = 0
        while True:
            if self.size() == 0:
                break
            val = self.dequeue()
            new_queue[i] = val
            i += 1
        self.queue = new_queue
        self.queue_len = len(self.queue)

        self.i_front = 0
        self.i_end = i-1  # 因為在最後一個while裡面有多加了1

    def dequeue(self):
        if self.size() == 0:
            return None
        elif self.size() == 1:
            val = self.queue[self.i_front]
            self.queue[self.i_front] = None
            self.i_front = None
            self.i_end = None
            return val
        else:
            val = self.queue[self.i_front]
            self.queue[self.i_front] = None
            self.i_front = (self.i_front + 1) % self.queue_len
            return val


if __name__ == "__main__":
    nums = [1,2,3,4,5]
    queue = MyQueue(nums)
    queue.build_queue()

    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()
    val = queue.dequeue()

    # empty
    val = queue.dequeue()

    queue.enqueue(11)
    queue.enqueue(12)
    queue.enqueue(13)
    queue.enqueue(14)
    queue.enqueue(15)

    # circular queue
    val = queue.dequeue()
    val = queue.dequeue()
    queue.enqueue(16)

    # expand queue
    for i in range(20):
        queue.enqueue(i)

    print(queue.queue)






