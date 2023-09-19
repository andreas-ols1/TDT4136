from Map import Map_Obj
from Heap import Min_Cell_Heap
from Cell import Cell
from typing import Callable


def h(current: list[int], goal: list[int]) -> int:
    """
    Heuristic function for A* algorithm
    Takes two positional arguments with list
    of coordinates and returns Manhattan distance
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def init_cells(a: Map_Obj) -> list[Cell]:
    """Initializes a 2D list of cells from a Map_Obj"""
    cells1 = []
    for i in range(len(a.get_maps()[0])):
        cells2 = []
        for j in range(len(a.get_maps()[0][0])):
            cells2.append(Cell([i, j], None, cost=a.get_cell_value([i, j])))
        cells1.append(cells2)
    return cells1


def reconstruct_path(current: Cell):
    path = [current]
    while current.parent:
        current = current.parent
        path.insert(0, current)
    return path


def attach_parent(child: Cell, parent: Cell, goal: list[int]):
    child.parent = parent
    child.update_g()
    child.update_h(h, goal)
    child.update_f()


def improve_path(cell: Cell):
    for child in cell.get_children():
        if cell.g + cell.get_cost() < child.g:
            child.parent = cell
            child.update_g()


def A_star(a: Map_Obj, h: Callable):
    """A* algorithm: Returns the shortest path from start to goal if it exists, otherwise false"""
    all_cells = init_cells(a)
    frontier = Min_Cell_Heap()
    visited = []
    start_cell = all_cells[a.get_start_pos()[0]][a.get_start_pos()[1]]
    frontier.insert(start_cell)

    while not frontier.is_empty():
        current_cell = frontier.extract_min()
        visited.append(current_cell)

        if current_cell.get_position() == a.get_goal_pos():
            return reconstruct_path(current_cell)

        current_cell.generate_children(all_cells)

        for child in current_cell.get_children():
            if child not in visited and child not in frontier:
                attach_parent(child, current_cell, a.get_goal_pos())
                frontier.insert(child)
            elif current_cell.g + current_cell.get_cost() < child.g:
                attach_parent(child, current_cell, a.get_goal_pos())
                if child in visited:
                    improve_path(child)

    return False


if __name__ == "__main__":
    a = Map_Obj(task=1)
    shortest_path = A_star(a, h)
    a.show_map(path=shortest_path)
