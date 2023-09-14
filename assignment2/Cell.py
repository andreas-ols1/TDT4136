class Cell:
    def __init__(self, position, parent, cost=-1):
        self.position = position
        self.f = 0
        self.g = 0
        self.h = 0
        self.parent = parent
        self.children = []
        self.cost = cost

    def __repr__(self):
        return f"{self.f}"

    def __eq__(self, other):
        return self.f == other.f

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f

    def __le__(self, other):
        return self.f <= other.f

    def check_neighbours(self, other):
        neigbours = []
        neigbours.append([self.position[0] - 1, self.position[1]])
        neigbours.append([self.position[0] + 1, self.position[1]])
        neigbours.append([self.position[0], self.position[1] + 1])
        neigbours.append([self.position[0], self.position[1] - 1])
        return other in neigbours
