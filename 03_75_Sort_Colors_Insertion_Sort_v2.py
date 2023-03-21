class Solution:

    def sortColors(self, nums):
        """
        重點：需要是in-place的排序
        Three colors: 0, 1, 2, and use 3 pointer to solve this problem.
        """

        l = 0
        r = len(nums) - 1
        p = 0  # current pointer

        while p <= r:

            if nums[p] == 0:
                nums[l], nums[p] = nums[p], nums[l]
                l += 1
                p += 1
            elif nums[p] == 2:
                nums[r], nums[p] = nums[p], nums[r]
                r -= 1
            else:
                p += 1


if __name__ == "__main__":

    nums = [2,0,2,1,1,0]
    Solution().sortColors(nums)
    print(nums)
