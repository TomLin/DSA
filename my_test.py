class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def insert(head):

    dummy = ListNode(val=-6000)
    dummy.next = head

    while True:
        pre = dummy
        cur = head
        while pre and cur and cur.next:
            if cur.next.val < cur.val:
                tmp = cur.next.next
                cur.next.next = cur
                pre.next = cur.next
                cur.next = tmp
                pre = pre.next.next
                cur = cur.next
            else:
                pre = cur
                cur = cur.next
        break

    return dummy.next



if __name__ == "__main__":

    cnt = 0
    val = 10
    head = ListNode(11)
    cur = head
    while cnt < 5:
        node = ListNode(val)
        cur.next = node
        cur = cur.next
        cnt += 1
        val -= 1

    print(head.val)
    insert(head)
    print(head.val)