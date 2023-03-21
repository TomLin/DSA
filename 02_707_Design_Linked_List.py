'''
解題思路:
1. 先創建Node物件
2. 再創造一個房屋(list)，來容納Node
3. 針對房屋，則是建立head, end, len等flag，幫助進行搜索
4. 先讓房屋內是None，而不先建立一個空的Node(這會讓後續解題簡單許多)
5. 例外處理，先思考例外，處理corner case，之後再處理common case，例外狀況包含…
    (a) 索取out of bound的index
    (b) head是None時
    (c) add node在頭時
    (d) add node在尾時
    (e) 再來則是common case: add node在中間時
    (f) 刪除中間node時
    (g) 刪除head的node時
    (g) 刪除完發現是空的房屋時
    (h) 刪除在end node時
'''


class Node:

    def __init__(self, val):

        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):

        self.head = None
        self.end = self.head
        self.len = 0

    def get(self, index: int) -> int:

        # 例外處理
        if index >= self.len:
            return -1

        cur = self.head
        cnt = 0
        while cnt < index:
            cur = cur.next
            cnt += 1
        return cur.val


    def addAtHead(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
            self.end = self.head
            self.len += 1

        else:
            temp = Node(val)
            temp.next = self.head
            self.head = temp
            self.len += 1

    def addAtTail(self, val: int) -> None:

        if self.head is None:
            self.head = Node(val)
            self.end = self.head
            self.len += 1

        else:
            self.end.next = Node(val)
            self.end = self.end.next
            self.len += 1

    def addAtIndex(self, index: int, val: int) -> None:

        # 例外處理
        if index > self.len:
            return

        if index == 0:
            self.addAtHead(val)

        elif index == self.len:
            self.addAtTail(val)

        else:
            cur = self.head
            cnt = 0
            while cnt < index:
                pre = cur
                cur = cur.next
                cnt += 1
            new = Node(val)
            new.next = cur
            pre.next = new
            self.len += 1


    def deleteAtIndex(self, index: int) -> None:

        if index >= self.len:
            return

        if index == 0:
            self.head = self.head.next
            self.len -= 1
            # 刪除完，發現房屋是空的時，需要再維護end的flag
            if self.len == 0:
                self.end = None

        else:
            cur = self.head
            cnt = 0
            while cnt < index:
                pre = cur
                cur = cur.next
                cnt += 1
            pre.next = cur.next
            if index == self.len-1:
                self.end = pre
            self.len -= 1
