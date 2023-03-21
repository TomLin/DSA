class Solution:
    
    def sortColors(self, nums):
        
        # 每次向左看(第0個位置，不需要向左看)
        for i_run in range(1, len(nums)):
            # 從第i_run的位置開始，往左比較，到index=1時
            # 每一次如果發現左邊的值比自己大，那就停止比較了
            for j in range(i_run,0,-1):
                if nums[j-1] > nums[j]:
                    temp = nums[j-1]
                    nums[j-1] = nums[j]
                    nums[j] = temp
                else:
                    # insertion sort的好處是，它不需要像bubble sort一樣，把全部的值看過一遍
                    # 在該run時，如果發現左邊的值比自己大，那就停止比較了
                    break