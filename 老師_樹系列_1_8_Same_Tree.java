public class Solution {
    public boolean isSameTree(TreeNode p, TreeNode q) {
        if (p == null && q == null) return true;
        if (p != null && q == null) return false;
        if (p == null && q != null) return false;

        boolean result = true;

        if (p.val != q.val) {
            result = false;
        }else {
            boolean result_left = isSameTree(p.left, q.left);
            if (result_left == false) result = false;
            boolean result_right = isSameTree(p.right, q.right);
            if (result_right == false) result = false;
        }


        return result;
    }
}