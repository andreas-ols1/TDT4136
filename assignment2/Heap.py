import heapq


class Min_Heap:
    """Min Heap data structure implementation using heapq module.

    Attributes:
        A: list of integers

    Methods:
        parent(i): returns the parent of the node
        right(i): returns the right child of the node
        left(i): returns the left child of the node
        min_heapify(i): heapifies the heap
        insert(i): inserts an element into the heap.
        extract_min(): extracts the minimum element from the heap"""

    def __init__(self):
        self.A = []

    def __len__(self):
        return len(self.A)

    def __repr__(self):
        return str(self.A)

    def parent(self, i):
        return i // 2

    def right(self, i):
        return 2 * i + 1

    def left(self, i):
        return 2 * i

    def min_heapify(self, i):
        heapq.heapify(self.A)

    def insert(self, a):
        heapq.heappush(self.A, a)

    def extract_min(self):
        return heapq.heappop(self.A)
