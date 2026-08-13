class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        n = len(s)
        # Tree node representations using arrays for optimal performance
        # Each index i represents a segment tree node:
        max_len = [0] * (4 * n)
        prefix_len = [0] * (4 * n)
        suffix_len = [0] * (4 * n)
        left_char = [''] * (4 * n)
        right_char = [''] * (4 * n)
        
        # Convert string to list for easy indexing
        chars = list(s)

        def merge(node, l, r, mid):
            left_node = 2 * node
            right_node = 2 * node + 1
            
            left_size = mid - l + 1
            right_size = r - mid
            
            left_char[node] = left_char[left_node]
            right_char[node] = right_char[right_node]
            
            # Default prefix/suffix lengths
            prefix_len[node] = prefix_len[left_node]
            suffix_len[node] = suffix_len[right_node]
            
            # Overall max length starts as max of children
            max_len[node] = max(max_len[left_node], max_len[right_node])
            
            # Check if middle boundary characters match
            if right_char[left_node] == left_char[right_node]:
                cross_len = suffix_len[left_node] + prefix_len[right_node]
                max_len[node] = max(max_len[node], cross_len)
                
                # If left segment is entirely same character
                if prefix_len[left_node] == left_size:
                    prefix_len[node] = left_size + prefix_len[right_node]
                    
                # If right segment is entirely same character
                if suffix_len[right_node] == right_size:
                    suffix_len[node] = right_size + suffix_len[left_node]

        def build(node, l, r):
            if l == r:
                max_len[node] = 1
                prefix_len[node] = 1
                suffix_len[node] = 1
                left_char[node] = chars[l]
                right_char[node] = chars[l]
                return
            
            mid = (l + r) // 2
            build(2 * node, l, mid)
            build(2 * node + 1, mid + 1, r)
            merge(node, l, r, mid)

        def update(node, l, r, idx, ch):
            if l == r:
                chars[l] = ch
                left_char[node] = ch
                right_char[node] = ch
                return
            
            mid = (l + r) // 2
            if idx <= mid:
                update(2 * node, l, mid, idx, ch)
            else:
                update(2 * node + 1, mid + 1, r, idx, ch)
                
            merge(node, l, r, mid)

        # Build initial segment tree
        build(1, 0, n - 1)
        
        ans = []
        for ch, idx in zip(queryCharacters, queryIndices):
            if chars[idx] != ch:
                update(1, 0, n - 1, idx, ch)
            ans.append(max_len[1])
            
        return ans