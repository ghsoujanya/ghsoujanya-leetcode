class Solution {
    private int maxDiameter = 0;

    public int diameterOfBinaryTree(TreeNode root) {
        getDepth(root);
        return maxDiameter;
    }

    private int getDepth(TreeNode node) {
        if (node == null) {
            return 0;
        }

        int leftDepth = getDepth(node.left);
        int rightDepth = getDepth(node.right);

        // The longest path passing through this node is left depth + right depth
        maxDiameter = Math.max(maxDiameter, leftDepth + rightDepth);

        // Return the height of the current subtree
        return 1 + Math.max(leftDepth, rightDepth);
    }
}