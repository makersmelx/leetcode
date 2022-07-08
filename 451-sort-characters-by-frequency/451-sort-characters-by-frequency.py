class Solution:
    def frequencySort(self, s: str) -> str:
        counter = collections.Counter(s)
        ret = []
        for k,v in sorted(counter.items(),key=lambda c: c[1], reverse=True):
            ret.append(k*v)
        return ''.join(ret)