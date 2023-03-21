public class Sort_Insertion3 {
    public static void insertion_sort(int[] nums) {
        for (int i_start = 0; i_start < nums.length; i_start++) {
            for (int j_run = i_start - 1; j_run >= 0; j_run--) {
                if (nums[j_run + 1] > nums[j_run]) {
                    swap(nums,j_run + 1, j_run);
                }else {
                    break;
                }
            }
        }
    }

    public static void insertion_sort_recursion(int[] nums) {

        int i_start = 0;
        insertion_sort_recursion_help01(nums, i_start);

    }

    private static void insertion_sort_recursion_help01(int[] nums, int i_start) {
        /** end condition **/
        if (i_start >= nums.length) {
            return;
        }

        /** main logic **/
        int j_run = i_start - 1;
        insertion_sort_recursion_help02(nums, j_run);

        /** data flow **/
        insertion_sort_recursion_help01(nums, i_start + 1);

    }

    private static void insertion_sort_recursion_help02(int[] nums, int j_run) {
        /** end condition **/
        if (j_run < 0) {
            return;
        }

        /** main logic **/
        if (nums[j_run + 1] > nums[j_run]) {
            swap(nums,j_run + 1, j_run);
        }else {
            return;
        }

        /** data flow **/
        insertion_sort_recursion_help02(nums, j_run - 1);
    }

    private static void swap(int[] nums, int i_left, int i_right) {
        int tmp = nums[i_left];
        nums[i_left] = nums[i_right];
        nums[i_right] = tmp;
    }

    public static void main(String[] args) {
        int[] nums = new int[]{8, 2, 6, 10, 4};
        Sort_Insertion3.insertion_sort(nums);

        System.out.println();

        nums = new int[]{8, 2, 6, 10, 4};
        Sort_Insertion3.insertion_sort_recursion(nums);

        System.out.println();
    }
}