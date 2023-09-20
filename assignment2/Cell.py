class Cell:
    """
    A class representing a cell in a grid for pathfinding algorithms.

    Attributes:
        position (tuple): The (x, y) coordinates of the cell.
        parent (Cell): The parent cell from which this cell is reached in the path.
        cost (int, optional): The cost associated with moving to this cell (default is -1).
        f (int): The total cost of the cell (g + h).
        g (int): The cost from the start node to this cell.
        h (int): The heuristic cost from this cell to the goal.
        children (list): List of neighboring cells that can be reached from this cell.

    Methods:
        generate_children(self, cells):
            Adds neighboring cells to the children list if they are not walls.

        update_h(self, h, goal):
            Updates the heuristic cost (h) of the cell based on a given heuristic function and a goal cell.

        update_g(self):
            Recalculates the cost from the start node to this cell (g) based on the parent's g value and the cell's cost.

        update_f(self):
            Recalculates the total cost of the cell (f) based on the updated g and h values.
    """

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
        """Adds neighbours to the children list if they are not walls"""
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
