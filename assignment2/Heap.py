from Cell import Cell


class Min_Cell_Heap:
    """Min Heap data structure implementation for nodes to be used as priority queue.

    Attributes:
        A: list of nodes

    Methods:
        parent(i): returns the parent of the node
        right(i): returns the right child of the node
        left(i): returns the left child of the node
        min_heapify(i): maintains the heap property
        insert(i): inserts an element into the heap.
        extract_min(): extracts the minimum element from the heap"""

    def __init__(self):
        """
        Initialize an empty Min_Cell_Heap.
        """
        self.A = []

    def __len__(self) -> int:
        return len(self.A)

    def __repr__(self) -> str:
        return str(self.A)

    def __contains__(self, x: Cell) -> bool:
        return x in self.A

    def parent(self, i: int) -> int:
        return i // 2

    def right(self, i) -> int:
        return 2 * i + 1

    def left(self, i: int) -> int:
        return 2 * i

    def min_heapify(self, i: int) -> None:
        """
        Ensure the heap property is maintained starting from the given index
        by recursively swapping elements with their minimum child, if necessary.

        This method is used internally to maintain the heap property after
        an element has been extracted or its key has been decreased.

        Args:
            index: The index of the element to start the heapify process from.
        """
        l = self.left(i)
        r = self.right(i)
        if l < len(self.A) and self.A[l] < self.A[i]:
            m = l
        else:
            m = i
        if r < len(self.A) and self.A[r] < self.A[m]:
            m = r
        if m != i:
            self.A[i], self.A[m] = self.A[m], self.A[i]
            self.min_heapify(m)

    def decrease_key(self, x: Cell, key: float) -> None:
        """
        Decrease the key of a specific element in the heap.

        Args:
            x: The element whose key needs to be decreased.
            key: The new key value to set for the element.
        """
        if key > x.f:
            raise ValueError("New key is larger than current key")
        x.f = key
        i = self.A.index(x)
        while self.A[self.parent(i)] > self.A[i]:
            self.A[i], self.A[self.parent(i)] = (
                self.A[self.parent(i)],
                self.A[i],
            )
            i = self.parent(i)

    def insert(self, x: Cell) -> None:
        """
        Insert a new element with the given key and value into the heap.

        Args:
           x: The cell to be inserted into the heap.
        """
        k = x.f
        x.f = float("inf")
        self.A.append(x)
        self.decrease_key(x, k)

    def heap_min(self) -> Cell:
        if not self.A:
            return None
        return self.A[0]

    def extract_min(self) -> Cell:
        """
        Remove and return the element with the minimum key from the heap.

        Returns:
            Cell: The Cell object containing the minimum key.
        """
        min = self.heap_min()
        self.A[0], self.A[-1] = self.A[-1], self.A[0]
        self.min_heapify(0)
        self.A.remove(min)
        return min

    def is_empty(self) -> bool:
        """
        Check if the heap is empty.

        Returns:
            bool: True if the heap is empty, False otherwise.
        """
        return not self.A
