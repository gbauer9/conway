import random

class Cell():
    def __init__(self, val):
        self.val = val

    def __repr__(self):
        return str(self.val)

    def __add__(self, other):
        return self.val + other.val

class Board():
    def __init__(self, size):
        self.state = [[Cell(random.randint(0, 1)) for _ in range(size)] for _ in range(size)]
        self.size = size

    def updateBoard(self):
        new_state = self.state.copy()

        for i in range(self.size):
            for j in range(self.size):
                pass
        return

    def __repr__(self):
        return '\n'.join([''.join(str(x)) for x in self.state])

b = Board(5)

print(b)