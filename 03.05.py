class SortedStack:

    def __init__(self):
        self.s1 = []
        self.s2 = []

    def push(self, val: int) -> None:
        if not self.s2 or (val <= self.s2[-1] and (not self.s1 or val >= self.s1[-1])):
            self.s2.append(val)
            # print(val)
        else:
            if self.s2[-1] <= val:
                while self.s2 and self.s2[-1] < val:
                    self.s1.append(self.s2.pop())
                self.s2.append(val)
            if self.s1[-1] >= val:
                while self.s1 and self.s1[-1] > val:
                    self.s2.append(self.s1.pop())
                self.s1.append(val)
        # print(self.s1, self.s2)

    def pop(self) -> None:
        self.move()
        if self.s2:
            self.s2.pop()

    def peek(self) -> int:
        self.move()
        if self.s2:
            return self.s2[-1]
        else:
            return -1

    def isEmpty(self) -> bool:
        return not self.s1 and not self.s2

    def move(self):
        while self.s1:
            self.s2.append(self.s1.pop())
        # print('move', self.s1, self.s2)

# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
