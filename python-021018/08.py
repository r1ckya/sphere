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

    @left.setter
    def left(self, other):
        self._left = other

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, other):
        self._right = other

    def empty(self):
        return self.value is None

    def append(self, value):
        if self.empty():
            self._value = value
            return

        if value < self.value:
            if self.left is None:
                self.left = type(self)(value)
            else:
                self.left.append(value)
        else:
            if self.right is None:
                self.right = type(self)(value)
            else:
                self.right.append(value)

    def __contains__(self, value):
        if self.empty():
            return False

        if value == self.value:
            return True
        elif value < self.value:
            return self.left.__contains__(value) if self.left else False
        else:
            return self.right.__contains__(value) if self.right else False

    def __iter__(self):
        if self.empty():
            return

        queue = deque()
        queue.append(self)

        while len(queue) > 0:
            cur = queue.popleft()
            yield cur.value
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)


if __name__ == '__main__':
    tree = BinarySearchTree()
    print(*tree)
    for v in [8, 3, 10, 1, 6, 4, 14, 13, 7]:
        tree.append(v)

    for v in [8, 12, 13]:
        print(v in tree)

    print(*tree)
