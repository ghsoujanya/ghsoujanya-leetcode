class Solution(object):
    def validSequence(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: List[int]
        """
        n, m = len(word1), len(word2)
        
        # last[j] stores the rightmost index in word1 where word2[j] can be matched
        # when matching the suffix word2[j..m-1] greedily from right to left.
        last = [-1] * m
        j = m - 1
        for i in range(n - 1, -1, -1):
            if j >= 0 and word1[i] == word2[j]:
                last[j] = i
                j -= 1
                
        res = []
        changed = False
        j = 0
        
        # Greedily match word2 from left to right in word1
        for i in range(n):
            if j == m:
                break
                
            if word1[i] == word2[j]:
                # If we already used our 1 character mismatch, verify that the
                # remaining suffix word2[j+1..m-1] can be matched after index i.
                if changed:
                    if j + 1 == m or last[j + 1] > i:
                        res.append(i)
                        j += 1
                else:
                    # Mismatch not used yet; matching an exact character is always optimal.
                    res.append(i)
                    j += 1
            else:
                # Character mismatch: if we haven't used our allowed 1 change yet,
                # check if changing word1[i] to word2[j] allows completing the remaining word2.
                if not changed:
                    if j + 1 == m or last[j + 1] > i:
                        res.append(i)
                        changed = True
                        j += 1
                        
        return res if len(res) == m else []