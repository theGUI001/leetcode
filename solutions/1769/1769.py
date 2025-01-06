class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        
        if n == 1:
            return [0]
        
        if n == 2:
            return [int(x) for x in list(boxes[::-1])]
        
        positions, results= [], []
        for i in range(n):
            if boxes[i] == "1":
                positions.append(i)
        for i in range(n):
            sm = 0
            for position in positions:
                distance = abs(i - position)
                sm += distance
            results.append(sm)
        return results
        