class RandomizedSet:

    def __init__(self):
        self.list = []
        self.map = {}

    def insert(self, val: int) -> bool:
        if val in self.map:
            return False
        
        self.map[val] = len(self.list)
        self.list.append(val)
        return True

    def remove(self, val: int) -> bool:
        if val in self.map:
            last_val = self.list[-1]
            remove_pos = self.map[val]
            self.list[remove_pos] = last_val
            self.map[last_val] = remove_pos
            self.list.pop()
            del self.map[val]
            return True
        
        return False

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()