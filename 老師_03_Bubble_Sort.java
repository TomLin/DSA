public class Sort_Bubble3 {

    // 在下面的bubble_sort，是使用迴圈的方式實作，
    // 可以看到第一圈round，就是整個list的長度，每一個element都會經過一個round，
    // 之後第二個圈，就是當然這個element和前一個element比較，如果前一個比較大，就交換，
    // 否則就是繼續跑，直到list的尾端
    public static void bubble_sort(int[] nums){
        for (int round = 0; round < nums.length; round++) {
            // int len = nums.length;
            int len = nums.length - round; // improved version
            for (int i_run = 1; i_run < len; i_run++) {
                if (nums[i_run - 1] > nums[i_run]) {
                    swap(nums, i_run - 1, i_run);
                }
            }
        }
    }

    public static void bubble_sort_recursion(int[] nums) {
        int round = 0;
        bubble_sort_recursion_help01(nums, round);
    }

    private static void bubble_sort_recursion_help01(int[] nums, int round) {
        /** end condition **/
        if (round >= nums.length) {
            return;
        }

        /** main logic **/
        int len = nums.length - round;
        int i_run = 1;
        bubble_sort_recursion_help02(nums, len, i_run);

        /** data flow **/
        bubble_sort_recursion_help01(nums, round + 1);
    }

    private static void bubble_sort_recursion_help02(int[] nums, int len, int i_run) {
        /** end condition **/
        if (i_run >= len) {
            return;
        }

        /** main logic **/
        if (nums[i_run - 1] > nums[i_run]) {
            swap(nums, i_run - 1, i_run);
        }

        /** data flow **/
        bubble_sort_recursion_help02(nums, len, i_run + 1);

    }

    private static void swap(int[] nums, int i_left, int i_right) {
        int tmp = nums[i_left];
        nums[i_left] = nums[i_right];
        nums[i_right] = tmp;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{8, 2, 6, 10, 4};
        Sort_Bubble3.bubble_sort(nums);

        System.out.println();

        nums = new int[]{8, 2, 6, 10, 4};
        Sort_Bubble3.bubble_sort_recursion(nums);

        System.out.println();
    }
}