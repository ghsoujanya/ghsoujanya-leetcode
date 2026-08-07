class Solution {
    public int maxDepth(TreeNode root) {
        // Base case: empty tree has a depth of 0
        if (root == null) {
            return 0;
        } 
        
        // Recursively compute the depth of left and right subtrees
        int leftDepth = maxDepth(root.left); 
        int rightDepth = maxDepth(root.right); 
        
        // Maximum depth is the max between left and right depth + 1 for the current node
        return Math.max(leftDepth, rightDepth) + 1; 
    } 
}