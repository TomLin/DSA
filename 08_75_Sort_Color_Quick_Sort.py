# Python 实现的十大经典排序算法
# https://leetcode-cn.com/problems/sort-an-array/solution/python-shi-xian-de-shi-da-jing-dian-pai-xu-suan-fa/

"""
Quick Sort的操作方式，基本上就像是pre-order的binary search tree的建立，因此可以把它們歸類在一起。
"""


class Solution:

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        i_left = 0
        i_right = len(nums) -1

        self.quick_sort(nums, i_left, i_right)

        return nums

    def quick_sort(self, nums, i_left, i_right):

        if i_right <= i_left:
            return

        i = i_left
        j = i_right
        pivot_val = nums[i_right]

        # 只要i和j還沒有碰到，就一直進行
        while i!=j:

            # 先針對i指針，往前走
            while (i < j) and (nums[i] < pivot_val):
                i += 1

            # 再針對j指針，往後退
            while (i < j) and (nums[j] >= pivot_val):
                j -= 1

            # 每一次i指針與j指針已經break的時候，就進行交換(這時因為i和j還沒有碰頭，所以等一下又會再進去while迴圈)
            if i < j:
                self.swap(nums, i, j)

        # 當i和j已經碰頭時，表示這個指針就是該pivot_val最適合的位置，再進行value的交換
        # 記得，每一次取出來的pivot_val，在每一次的比較中，都會幫它決定最適合的位置(在array當中)
        # 如果pivot_val在中間，那當然就是交換，i和j會相交於中間
        # 如果pivot_val為最大，那最後i和j就會相交於最後一個位置
        # 如果pivot_val為最小，那最後i和j就會相交於第一個位置
        # 而這個i，就是下一輪放入函數，當作是pivot位置的index
        self.swap(nums, i, i_right)

        self.quick_sort(nums, i_left, i-1)
        self.quick_sort(nums, i+1, i_right)

    def swap(self, nums, i, j):

        nums[i], nums[j] = nums[j], nums[i]
