class OrderedStream:

    def __init__(self, n: int):
        self.seen = {}
        self.itr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.seen[idKey] = value
        result = []
        while self.itr in self.seen:
            result.append(self.seen[self.itr])
            del self.seen[self.itr]
            self.itr += 1
            
        return result


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)