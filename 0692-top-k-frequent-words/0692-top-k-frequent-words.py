from collections import Counter
import heapq

class Pair:
    def __init__(self, word: str, count: int):
        self.word = word
        self.count = count

    def __lt__(self, other):
        # Min-Heap comparator logic:
        # 1. Lower count has higher priority to be popped first.
        # 2. If counts are equal, lexicographically larger word has higher priority 
        #    to be popped first (so smaller words stay in the heap).
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

class Solution:
    def topKFrequent(self, words: list[str], k: int) -> list[str]:
        # Step 1: Count word frequencies - O(N) time, O(N) space
        freq = Counter(words)
        
        # Step 2: Maintain a Min-Heap of size k - O(N log k) time, O(k) space
        heap = []
        for word, count in freq.items():
            heapq.heappush(heap, Pair(word, count))
            if len(heap) > k:
                heapq.heappop(heap)
        
        # Step 3: Extract elements and reverse to get highest frequency first
        result = []
        while heap:
            result.append(heapq.heappop(heap).word)
            
        return result[::-1]