import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from copy import deepcopy

class Board():
    def __init__(self, init):
        if isinstance(init, int):
            self.state = [[random.randint(0, 1) for _ in range(init)] for _ in range(init)]
            self.size = init
        elif isinstance(init, list) and isinstance(init[0], list) and len(init) == len(init[0]):
            self.state = init
            self.size = len(init)
        else:
            raise TypeError("Board initialization must be an int representing the (square) dimensions or a 2d array")

    def updateBoard(self, *args):
        new_state = deepcopy(self.state)
        num_neighbors = 0

        for i in range(self.size):
            for j in range(self.size):
                num_neighbors = sum([self.state[(i-1) % self.size][(j-1) % self.size], 
                self.state[(i-1) % self.size][j], 
                self.state[(i-1) % self.size][(j+1) % self.size], 
                self.state[i][(j-1) % self.size], 
                self.state[i][(j+1) % self.size], 
                self.state[(i+1) % self.size][(j-1) % self.size],
                self.state[(i+1) % self.size][j],
                self.state[(i+1) % self.size][(j+1) % self.size]])
                
                if self.state[i][j] == 1 and (num_neighbors > 3 or num_neighbors < 2):
                    new_state[i][j] = 0
                elif self.state[i][j] == 0 and num_neighbors == 3:
                    new_state[i][j] = 1
                else:
                    new_state[i][j] = self.state[i][j]

        self.state = new_state
        scene.set_array(self.state)
        return scene,

    def __repr__(self):
        return '\n'.join([''.join(str(x)) for x in self.state])

    def __getitem__(self, key):
        return self.state[key]

#b = Board([[0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])
b = Board(10)

fig = plt.figure()
scene = plt.imshow(b.state, animated=True)
ani = animation.FuncAnimation(fig, b.updateBoard, interval=500, blit=True)
plt.show()