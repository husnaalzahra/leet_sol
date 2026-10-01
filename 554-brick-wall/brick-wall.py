from typing import List
from collections import defaultdict

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        edge_count = defaultdict(int)
        
        for row in wall:
            current_pos = 0
            # Exclude the last brick since the rightmost boundary is not a valid cutting line
            for brick in row[:-1]:
                current_pos += brick
                edge_count[current_pos] += 1
                
        # Find the maximum number of times an edge aligns vertically
        max_edges = max(edge_count.values()) if edge_count else 0
        
        # Minimum crossed bricks = Total rows - Max aligned edges
        return len(wall) - max_edges