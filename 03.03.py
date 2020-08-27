class StackOfPlates:

    def __init__(self, cap: int):
        self._cap = cap
        self.stacks = []

    def push(self, val: int) -> None:
        if self._cap == 0:
            return
        if not self.stacks or len(self.stacks[-1]) == self._cap:
            self.stacks.append([val])
        else:
            self.stacks[-1].append(val)

    def pop(self) -> int:
        if not self.stacks:
            return -1
        val = self.stacks[-1].pop()
        if not self.stacks[-1]:
            self.stacks.pop()
        return val

    def popAt(self, index: int) -> int:
        if index > len(self.stacks) - 1:
            return -1
        val = self.stacks[index].pop()
        if not self.stacks[index]:
            self.stacks.pop(index)
        return val


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)