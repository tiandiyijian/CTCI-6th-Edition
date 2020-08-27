class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self._s = []
        self._m = []

    def push(self, x: int) -> None:
        self._s.append(x)
        if not self._m or x <= self._m[-1]:
            self._m.append(x)

    def pop(self) -> None:
        if self._s:
            x = self._s.pop()
            if x == self._m[-1]:
                self._m.pop()

    def top(self) -> int:
        if self._s:
            return self._s[-1]

    def getMin(self) -> int:
        return self._m[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
