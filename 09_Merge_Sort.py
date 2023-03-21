"""
針對三指針用法的參考資料：
https://leetcode-cn.com/problems/sort-colors/solution/75-yan-se-fen-lei-pythonzhi-zhen-yi-bian-0vct/
https://medium.com/@ryanyang1221/leetcode-challenge-sort-colors-6-11-35b06bb229cb

"""

# Python type hint的簡易使用與介紹
# https://myapollo.com.tw/zh-tw/python-typing-module/

# 寫的簡單易懂的merge sort
# https://ithelp-ithome-com-tw.translate.goog/articles/10278179?_x_tr_sl=zh-TW&_x_tr_tl=en&_x_tr_hl=en&_x_tr_pto=sc

from typing import List

class Solution:
    def mergeSort(self, nums: List[int]) -> List[int]:

        return self.divide(nums)

    def divide(self, nums):

        if len(nums) <= 1:
            return nums  # 切到只剩下一個元素時，需要回傳這個元素

        # 尋找array中間點，來對切
        mid_idx = len(nums) // 2
        left = nums[:mid_idx]
        right = nums[mid_idx:]

        n_left = self.divide(left)
        n_right = self.divide(right)

        # 類似post-order的精神，當子樹的結果，要回傳給母樹時，進行合併的操作
        return self.merge(n_left, n_right)

    def merge(self, left, right):

        i = 0
        j = 0

        merge_ls = []

        # 兩個array進行合併時，使用while的寫法，比較簡潔
        while i < len(left) and j < len(right):

            if left[i] <= right[j]:
                merge_ls.append(left[i])
                i += 1
            else:
                merge_ls.append(right[j])
                j += 1

        # 把剩下的array，append到merge array上頭
        if i < len(left):
            merge_ls = merge_ls + left[i:]
        if j < len(right):
            merge_ls = merge_ls + right[j:]
        return merge_ls


if __name__ == "__main__":

    nums = [5,1,2,9,0,2,8,1,8,6,4]
    print("Before sort:\t", nums)
    solution = Solution()
    new_nums = solution.mergeSort(nums)
    print("After sort:\t", new_nums)