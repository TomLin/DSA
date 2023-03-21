class MyArray:

    def __init__(self, size):
        self.arr = [None] * size  # 學習如其它正規語言，需要設定list的長度
        self.i_end = -1  # idx, flag for indicating 值已經塞滿了list的空間

    def expand_space(self):
        # 當array的長度不夠時，直接創造一個兩倍長度的array，並且將值複製過去
        arr_new = [None] * (len(self.arr) * 2)
        for i in range(len(self.arr)):
            arr_new[i] = self.arr[i]

        self.arr = arr_new

    def add_by_idx(self, i_add, val):
        # time complexity: O(N)
        if self.i_end + 1 == len(self.arr):
            self.expand_space()

        # i_add 之後的值，都往後移一位
        for i in range(self.i_end, i_add-1, -1):
            self.arr[i+1] = self.arr[i]
            self.arr[i] = None

        self.arr[i_add] = val
        self.i_end += 1

    def add_by_val(self, val):
        # time complexity: O(1) -> 在array的空間夠的情況下
        self.add_by_idx(self.i_end+1, val)

    def search_by_idx(self, idx):
        # time complexity: O(1)
        if (idx > self.i_end) or (idx < 0):
            # corner case 的處理
            return None
        return self.arr[idx]


    def search_by_val(self, val):
        # time complexity: O(N)
        for i in range(self.i_end):
            if self.arr[i] == val:
                return val
        return None

    def remove_by_idx(self, idx):
        # time complexity: O(N)
        if (idx > self.i_end) or (idx < 0):
            # corner case 的處理
            return None

        for i in range(idx, self.i_end):
            self.arr[i] = self.arr[i+1]
            self.arr[i+1] = None

        self.i_end -= 1

    def remove_by_val(self, val):
        # time complexity: O(N)
        for i in range(self.i_end):
            if self.arr[i] == val:
                self.remove_by_idx(i)



if __name__ == "__main__":

    arr_obj = MyArray(5)

    arr_obj.add_by_val(9)
    arr_obj.add_by_val(11)
    arr_obj.add_by_val(2)
    arr_obj.add_by_val(98)
    arr_obj.add_by_val(35)

    arr_obj.add_by_val(44)

    i_add = 1
    arr_obj.add_by_idx(i_add, 50)

    val001 = arr_obj.search_by_val(2882)

    val002 = arr_obj.search_by_idx(4)

    arr_obj.remove_by_val(2)

    i_remove = 3
    arr_obj.remove_by_idx(i_remove)

