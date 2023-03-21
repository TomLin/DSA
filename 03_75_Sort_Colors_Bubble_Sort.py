class Solution:

    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """

        # 在下面的bubble_sort，是使用迴圈的方式實作，
        # 可以看到第一圈round，就是整個list的長度，每一個element都會經過一個round，
        # 之後第二個圈，就是當然這個element和前一個element比較，如果前一個比較大，就交換，
        # 否則就是繼續跑，直到list的尾端
        new_len = len(nums)
        for i in range(len(nums)):
            for j in range(1, new_len):
                if nums[j-1] > nums[j]:
                    temp = nums[j]
                    nums[j] = nums[j-1]
                    nums[j-1] = temp
            new_len -= 1