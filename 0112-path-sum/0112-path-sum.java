class Solution {
    public boolean hasPathSum(TreeNode root, int targetSum) {
        if (root == null) {
            return false;
        }
        
        // If it's a leaf node, check if the remaining targetSum equals the node's value
        if (root.left == null && root.right == null) {
            return targetSum == root.val;
        }
        
        // Recursively check left and right subtrees with updated target sum
        int remainingSum = targetSum - root.val;
        return hasPathSum(root.left, remainingSum) || hasPathSum(root.right, remainingSum);
    }
}