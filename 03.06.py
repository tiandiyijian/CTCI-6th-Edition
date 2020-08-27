import collections


class AnimalShelf:

    def __init__(self):
        self._dog = collections.deque()
        self._cat = collections.deque()

    def enqueue(self, animal: List[int]) -> None:
        if animal[1] == 0:
            self._cat.append(animal)
        else:
            self._dog.append(animal)

    def dequeueAny(self) -> List[int]:
        if not self._dog and not self._cat:
            return [-1, -1]
        elif self._dog and self._cat:
            if self._dog[0][0] < self._cat[0][0]:
                return self._dog.popleft()
            else:
                return self._cat.popleft()
        else:
            return self._dog.popleft() if self._dog else self._cat.popleft()
            

    def dequeueDog(self) -> List[int]:
        return self._dog.popleft() if self._dog else [-1, -1]

    def dequeueCat(self) -> List[int]:
        return self._cat.popleft() if self._cat else [-1, -1]


# Your AnimalShelf object will be instantiated and called as such:
# obj = AnimalShelf()
# obj.enqueue(animal)
# param_2 = obj.dequeueAny()
# param_3 = obj.dequeueDog()
# param_4 = obj.dequeueCat()