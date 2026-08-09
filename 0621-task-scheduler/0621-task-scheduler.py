from collections import Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count frequency of each task
        counts = Counter(tasks)
        max_freq = max(counts.values())
        
        # Count how many tasks have the maximum frequency
        max_freq_count = list(counts.values()).count(max_freq)
        
        # Calculate minimum slots based on maximum frequency tasks:
        # We need (max_freq - 1) groups of size (n + 1), plus the max_freq_count tasks at the end.
        ans = (max_freq - 1) * (n + 1) + max_freq_count
        
        # If the number of tasks is greater than the calculated slots, 
        # we don't need any idle time and can fit all tasks into len(tasks) intervals.
        return max(len(tasks), ans)