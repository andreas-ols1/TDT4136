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
        return f"Cell({self.position}, {self.parent}, {self.cost}, {self.f})"

    def __eq__(self, other):
        return self.position == other.position

    def __lt__(self, other):
        return self.f < other.f

    def __gt__(self, other):
        return self.f > other.f

    def __ge__(self, other):
        return self.f >= other.f

    def __le__(self, other):
        return self.f <= other.f

    def get_position(self):
        return self.position

    def get_cost(self):
        return self.cost

    def get_children(self):
        return self.children

    def get_g(self):
        return self.g

    def get_h(self):
        return self.h

    def get_f(self):
        return self.f

    def get_parent(self):
        return self.parent

    def generate_children(self, cells):
        neighbours = []
        neighbours.append(cells[self.position[0] - 1][self.position[1]])
        neighbours.append(cells[self.position[0] + 1][self.position[1]])
        neighbours.append(cells[self.position[0]][self.position[1] - 1])
        neighbours.append(cells[self.position[0]][self.position[1] + 1])
        for neighbour in neighbours:
            if neighbour.cost != -1:
                self.children.append(neighbour)

    def update_h(self, h, goal):
        self.h = h(self.position, goal)

    def update_g(self):
        self.g = self.parent.g + self.cost

    def update_f(self):
        self.f = self.g + self.h
