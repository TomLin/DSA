class BubbleSort:

    def __init__(self, array):

        self.arr = array
        self.length = len(self.arr)

    def bubble_sort(self):
        for i in range(self.length):
            left_round = self.length - i
            for j in range(1, left_round):
                if self.arr[j-1] > self.arr[j]:
                    self.swap(j-1, j)

    def swap(self, i_left, i_right):
        tmp = self.arr[i_left]
        self.arr[i_left] = self.arr[i_right]
        self.arr[i_right] = tmp


if __name__ == "__main__":

    nums = [4,7,1,2,9,3,5]
    my_sort = BubbleSort(nums)
    my_sort.bubble_sort()
    print(my_sort.arr)
