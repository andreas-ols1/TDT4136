from Map import Map_Obj
from Heap import Min_Cell_Heap
from Cell import Cell
from typing import Callable


def h(current: list[int], goal: list[int]) -> int:
    """
    Heuristic function for A* algorithm.

    Args:
        current (list[int]): The current node's coordinates [x, y].
        goal (list[int]): The goal node's coordinates [x, y].

    Returns:
        int: The Manhattan distance between the current node and the goal node.
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def init_cells(a: Map_Obj) -> list[Cell]:
    """
    Initializes a 2D list of cells from a Map_Obj.

    Args:
        a (Map_Obj): The map object containing map data.

    Returns:
        list[Cell]: A 2D list of initialized Cell objects.
    """
    cells1 = []
    for i in range(len(a.get_maps()[0])):
        cells2 = []
        for j in range(len(a.get_maps()[0][0])):
            cells2.append(Cell([i, j], None, cost=a.get_cell_value([i, j])))
        cells1.append(cells2)
    return cells1


def reconstruct_path(current: Cell) -> list[Cell]:
    """
    Reconstructs the path from the current cell to the start cell.

    Args:
        current (Cell): The current cell.

    Returns:
        list[Cell]: A list of cells representing the path from start to current cell.
    """
    path = [current]
    while current.parent:
        current = current.parent
        path.insert(0, current)
    return path


def attach_parent(child: Cell, parent: Cell, goal: list[int]) -> None:
    """
    Attaches a parent cell to a child cell, and updates the child's g, h, and f values.

    Args:
        child (Cell): The child cell.
        parent (Cell): The parent cell.
        goal (list[int]): The goal node's coordinates [x, y].
    """
    child.parent = parent
    child.update_g()
    child.update_h(h, goal)
    child.update_f()


def improve_path(cell: Cell) -> None:
    """
    Improves the path for a given cell by considering its children.

    Args:
        cell (Cell): The cell for which to improve the path.
    """
    for child in cell.get_children():
        if cell.g + cell.get_cost() < child.get_g():
            child.parent = cell
            child.update_g()


def A_star(a: Map_Obj, h: Callable) -> list[Cell] | bool:
    """
    A* algorithm: Returns the shortest path from start to goal if it exists, otherwise False.

    Args:
        a (Map_Obj): The map object containing map data.
        h (Callable): The heuristic function to estimate the cost from a node to the goal.

    Returns:
        list[Cell] | bool: A list of cells representing the shortest path or False if no path is found.
    """
    all_cells = init_cells(a)
    frontier = Min_Cell_Heap()
    visited = []
    start_cell = all_cells[a.get_start_pos()[0]][a.get_start_pos()[1]]
    frontier.insert(start_cell)

    while not frontier.is_empty():
        current_cell = frontier.extract_min()
        visited.append(current_cell)

        # Return the path if the current cell is the goal cell
        if current_cell.get_position() == a.get_goal_pos():
            return reconstruct_path(current_cell)

        current_cell.generate_children(all_cells)

        for child in current_cell.get_children():
            # If the child is not in the visited list or the frontier, add it to the frontier
            if child not in visited and child not in frontier:
                attach_parent(child, current_cell, a.get_goal_pos())
                frontier.insert(child)
            # If the child is in the frontier and the current path is better than the previous path, update the child
            elif current_cell.g + current_cell.get_cost() < child.get_g():
                attach_parent(child, current_cell, a.get_goal_pos())
                if child in visited:
                    improve_path(child)

    return False


if __name__ == "__main__":
    a = Map_Obj(task=4)
    shortest_path = A_star(a, h)
    a.save_map(path=shortest_path, location="visualisations/task4.png")
    # a.show_map(path=shortest_path)
