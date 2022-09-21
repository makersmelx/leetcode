class Node:
    def __init__(self, w, c):
        self.w = w
        self.c = c

    def __lt__(self, other):
        if self.c == other.c:
            return self.w > other.w
        else:
            return self.c < other.c
class Solution:
        
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = collections.Counter()
        for w in words:
            counter[w] += 1
        heap = []
        for w,c in counter.items():
            heapq.heappush(heap, Node(w,c))
            while len(heap) > k:
                heapq.heappop(heap)
        
        result = list()
        while heap:
            result.append(heappop(heap).w)
        return result[::-1]