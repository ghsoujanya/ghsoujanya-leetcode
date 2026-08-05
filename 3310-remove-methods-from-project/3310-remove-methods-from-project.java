import java.util.*;

class Solution {
    public List<Integer> remainingMethods(int n, int k, int[][] invocations) {
        // Step 1: Build adjacency list
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            graph.add(new ArrayList<>());
        }
        for (int[] inv : invocations) {
            graph.get(inv[0]).add(inv[1]);
        }

        // Step 2: BFS from node k to find all suspicious methods
        boolean[] isSuspicious = new boolean[n];
        Queue<Integer> queue = new ArrayDeque<>();
        
        queue.offer(k);
        isSuspicious[k] = true;

        while (!queue.isEmpty()) {
            int curr = queue.poll();
            for (int neighbor : graph.get(curr)) {
                if (!isSuspicious[neighbor]) {
                    isSuspicious[neighbor] = true;
                    queue.offer(neighbor);
                }
            }
        }

        // Step 3: Check if any non-suspicious node invokes a suspicious node
        for (int[] inv : invocations) {
            int u = inv[0];
            int v = inv[1];
            // If u is regular and v is suspicious, we cannot remove suspicious methods
            if (!isSuspicious[u] && isSuspicious[v]) {
                List<Integer> allMethods = new ArrayList<>();
                for (int i = 0; i < n; i++) {
                    allMethods.add(i);
                }
                return allMethods;
            }
        }

        // Step 4: Return only remaining non-suspicious methods
        List<Integer> result = new ArrayList<>();
        for (int i = 0; i < n; i++) {
            if (!isSuspicious[i]) {
                result.add(i);
            }
        }
        return result;
    }
}