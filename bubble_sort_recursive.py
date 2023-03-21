# 嘗試用recursive的方式，來寫bubble sort

class BubbleSort:

    def __init__(self, array):
        self.arr = array
        self.length = len(self.arr)

    def recur_sort(self, left_round=None):

        if left_round is None:
            left_round = self.length

        # Base case
        if left_round == 1:
            return

        for compare in range(1, left_round):
            if self.arr[compare-1] > self.arr[compare]:
                self.swap(compare-1, compare)

        self.recur_sort(left_round-1)

    def swap(self, i_left, i_right):
        tmp = self.arr[i_left]
        self.arr[i_left] = self.arr[i_right]
        self.arr[i_right] = tmp

if __name__ == "__main__":

    my_sort = BubbleSort([2,6,1,4,3,7,5])
    my_sort.recur_sort()
    print(my_sort.arr)
