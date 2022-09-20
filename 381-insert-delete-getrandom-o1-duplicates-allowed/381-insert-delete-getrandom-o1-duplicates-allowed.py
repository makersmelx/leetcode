class RandomizedCollection:

    def __init__(self):
        self.nums = []
        self.index = defaultdict(set)

    def insert(self, val: int) -> bool:
        old_size = len(self.index[val])
        self.index[val].add(len(self.nums))
        self.nums.append(val)
        return old_size == 0

    def remove(self, val: int) -> bool:
        if self.index[val]:
            out, replace = self.index[val].pop(), self.nums[-1]
            self.nums[out] = replace
            self.index[replace].add(out)
            self.index[replace].discard(len(self.nums) - 1)
            self.nums.pop()
            return True
        return False
            
        

    def getRandom(self) -> int:
        return random.choice(self.nums)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()