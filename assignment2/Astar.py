from Map import Map_Obj
from Heap import Min_Cell_Heap
from Cell import Cell

a = Map_Obj(task=1)


def h(current: list[int, int], goal: list[int, int]) -> int:
    """
    Heuristic function for A* algorithm
    Takes two positional arguments with list
    of coordinates and returns Manhattan distance
    """
    return abs(current[0] - goal[0]) + abs(current[1] - goal[1])


def A_star(a: Map_Obj):
    frontier = Min_Cell_Heap()
    visited = []

    frontier.insert(Cell(a.get_start_pos, h(a.get_start_pos, a.get_goal_pos)))

    while not frontier.is_empty():
        q = frontier.extract_min()

        for successor in q.get_neighbours():
            if successor.position == a.get_goal_pos():
                path.append(successor)
                return path
            successor.f == h(successor.position, a.get_goal_pos) + (
                q.g + successor.g
            )

            skip = False

            for p in frontier.A:
                if p.position == successor.position and p.f <= successor.f:
                    skip = True
                    break

            if skip:
                continue

            for p in path:
                if p.position == successor.position and p.f <= successor.f:
                    skip = True
                    break

            if skip:
                continue

            frontier.insert(successor)

        path.append(q)
