
class Solution {
    public int countNodes(TreeNode root) {
        if (root == null) {
            return 0;
        }

        int leftHeight = getLeftHeight(root.left);
        int rightHeight = getLeftHeight(root.right);

        // If heights are equal, left subtree is a full perfect tree
        if (leftHeight == rightHeight) {
            return (1 << leftHeight) + countNodes(root.right);
        } else {
            // Otherwise, right subtree is a full perfect tree of depth rightHeight
            return (1 << rightHeight) + countNodes(root.left);
        }
    }

    private int getLeftHeight(TreeNode node) {
        int height = 0;
        while (node != null) {
            height++;
            node = node.left;
        }
        return height;
    }
}