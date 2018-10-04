from collections import deque


class BinarySearchTree:
    def __init__(self, value=None):
        self._value = value
        self._left = None
        self._right = None

    @property
    def value(self):
        return self._value

    @property
    def left(self):
        return self._left

    @property
    def right(self):
        return self._right

    def empty(self):
        return self._value is None

    def append(self, value):
        if self.empty():
            self._value = value
            return

        if value < self._value:
            if self._left is None:
                self._left = type(self)(value)
            else:
                self._left.append(value)
        else:
            if self._right is None:
                self._right = type(self)(value)
            else:
                self._right.append(value)

    def __contains__(self, value):
        if self.empty():
            return False

        if value == self._value:
            return True
        elif value < self._value:
            return self._left.__contains__(value) if self._left is not None else False
        else:
            return self._right.__contains__(value) if self._right is not None else False

    def __iter__(self):
        if self.empty():
            return

        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            cur = queue.popleft()
            yield cur._value
            if cur._left:
                queue.append(cur._left)
            if cur._right:
                queue.append(cur._right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    print(*tree)
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)

    for v in [8, 12, 13]:
        print(v in tree)

    print(*tree)
