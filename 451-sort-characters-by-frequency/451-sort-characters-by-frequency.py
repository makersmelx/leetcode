class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter()
        
        for c in s:
            counter[c] += 1
        
        return sorted(s,key=lambda c: (counter[c],c), reverse=True)