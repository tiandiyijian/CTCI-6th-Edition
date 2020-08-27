class TripleInOne:

    def __init__(self, stackSize: int):
        self._nums = [None] * (stackSize * 3)
        self._peeks = [i * stackSize - 1 for i in range(3)]
        self._size = stackSize

    def push(self, stackNum: int, value: int) -> None:
        if self._peeks[stackNum] == (stackNum + 1) * self._size - 1:
            return
        self._peeks[stackNum] += 1
        self._nums[self._peeks[stackNum]] = value

    def pop(self, stackNum: int) -> int:
        if self._peeks[stackNum] == stackNum * self._size - 1:
            return -1
        self._peeks[stackNum] -= 1
        return self._nums[self._peeks[stackNum] + 1]

    def peek(self, stackNum: int) -> int:
        if self._peeks[stackNum] == stackNum * self._size - 1:
            return -1
        return self._nums[self._peeks[stackNum]]

    def isEmpty(self, stackNum: int) -> bool:
        return self._peeks[stackNum] == stackNum * self._size - 1


if __name__ == "__main__":
    # Your TripleInOne object will be instantiated and called as such:
    # obj = TripleInOne(stackSize)
    # obj.push(stackNum,value)
    # param_2 = obj.pop(stackNum)
    # param_3 = obj.peek(stackNum)
    # param_4 = obj.isEmpty(stackNum)
    pass
