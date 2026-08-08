class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return None

        # Hash map to map original node -> cloned node
        old_to_new = {}

        def dfs(curr):
            # Return clone if already created
            if curr in old_to_new:
                return old_to_new[curr]

            # Create clone for current node and map it
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Recursively clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)