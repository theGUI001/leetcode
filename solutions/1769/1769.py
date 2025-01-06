class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        if n == 1:
            return [0]
        
        if n == 2:
            return [int(x) for x in list(boxes[::-1])]
        
        results = [0] * n
        for current_box in range(n):
            if boxes[current_box] == "1":
                for new_position in range(n):
                    results[new_position] += abs(new_position - current_box)
        return results