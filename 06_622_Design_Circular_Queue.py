class MyCircularQueue:
    '''
    在queue的設計中，常常會搭配上循環的用法(circular queue)，也就是queued的尾巴，接上它的頭。
    通常這個實作，是會使用array實現(因為array的長度有限度，需要把空下來的空間再利用)，而不需要使用linked list。
    基本操作:
    - enqueue/offer: 就是add
    - dequeue/poll: 就是remove
    '''

    def __init__(self, k: int):
        '''
        將head初始化為0，tail初始化為負1，因為queue都是從tail開始加值上去，所以初始化令tail為-1的話，
        加一個值之後，tail的index就會和head的index值相同，表示現在queue裡面剛好有一個元素(這時候head和tail的index會是一樣的)
        '''
        self.arr = [None] * k
        self.head = 0
        self.tail = -1
        self.k = k  # k這個flag來知道這個array有多大
        self.len = 0  # len這個flag，來知道目前array存有幾個值

    def enQueue(self, value: int) -> bool:

        if self.isFull():
            return False
        else:
            self.tail = (self.tail + 1) % self.k
            self.arr[self.tail] = value
            self.len += 1
            return True

    def deQueue(self) -> bool:
        '''
        這邊設計的queue，如果已經全都被刪完了之後，head的index會比tail的index多加1(兩個值都不會再歸零)，
        之後再enQueue時，index數值再繼續往上加，這不影響queue的執行。
        '''
        if self.isEmpty():
            return False
        else:
            self.head = (self.head + 1) % self.k
            self.len -= 1
            return True

    def Front(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.arr[self.head]

    def Rear(self) -> int:

        if self.isEmpty():
            return -1
        else:
            return self.arr[self.tail]

    def isEmpty(self) -> bool:

        if self.len == 0:
            return True
        else:
            return False

    def isFull(self) -> bool:

        if self.len == self.k:
            return True
        else:
            return False