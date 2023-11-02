class Solution {

    public int averageOfSubtree(TreeNode root) {
        return helper(root)[2];
    }

    public int[] helper(TreeNode root) {
        if(root == null) return new int[] {0, 0, 0};

        int[] left = helper(root.left);
        int[]  right = helper(root.right);
        
        int sum = left[0] + right[0] + root.val;
        int count = left[1] + right[1] + 1;
        
        return new int[] {sum, count, left[2] + right[2]  + (sum/count == root.val ? 1 : 0)};
    }
}
