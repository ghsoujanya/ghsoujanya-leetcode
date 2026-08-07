import java.util.HashMap;
import java.util.Map;

class Solution {
    public int pathSum(TreeNode root, int targetSum) {
        Map<Long, Integer> prefixSumMap = new HashMap<>();
        // Base case: a prefix sum of 0 has occurred once (for paths starting at root)
        prefixSumMap.put(0L, 1);
        
        return dfs(root, 0L, targetSum, prefixSumMap);
    }
    
    private int dfs(TreeNode node, long currentSum, int targetSum, Map<Long, Integer> prefixSumMap) {
        if (node == null) {
            return 0;
        }
        
        // Update current running sum using long to prevent integer overflow
        currentSum += node.val;
        
        // Number of paths ending at the current node that sum to targetSum
        int count = prefixSumMap.getOrDefault(currentSum - targetSum, 0);
        
        // Add currentSum to hashmap for children to use
        prefixSumMap.put(currentSum, prefixSumMap.getOrDefault(currentSum, 0) + 1);
        
        // Recurse on left and right children
        count += dfs(node.left, currentSum, targetSum, prefixSumMap);
        count += dfs(node.right, currentSum, targetSum, prefixSumMap);
        
        // Backtrack: remove currentSum count so it doesn't affect parallel branches
        prefixSumMap.put(currentSum, prefixSumMap.get(currentSum) - 1);
        
        return count;
    }
}