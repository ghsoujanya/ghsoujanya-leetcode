import java.util.ArrayList;
import java.util.List;

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        List<Integer> currentPath = new ArrayList<>();
        backtrack(root, targetSum, currentPath, result);
        return result;
    }

    private void backtrack(TreeNode node, int remainingSum, List<Integer> currentPath, List<List<Integer>> result) {
        if (node == null) {
            return;
        }

        // Add the current node's value to the path
        currentPath.add(node.val);

        // Check if it's a leaf node and the remaining sum equals node.val
        if (node.left == null && node.right == null && remainingSum == node.val) {
            result.add(new ArrayList<>(currentPath)); // Create a copy of currentPath
        } else {
            // Recurse on left and right subtrees with the updated remaining sum
            backtrack(node.left, remainingSum - node.val, currentPath, result);
            backtrack(node.right, remainingSum - node.val, currentPath, result);
        }

        // Backtrack: remove the current node value before moving up the recursion tree
        currentPath.remove(currentPath.size() - 1);
    }
}