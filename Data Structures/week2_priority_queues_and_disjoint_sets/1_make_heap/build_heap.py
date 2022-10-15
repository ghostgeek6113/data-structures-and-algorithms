# python3

"""Converts an array of integers into a min-heap.
A binary heap is a complete binary tree which satisfies the heap ordering
property: the value of each node is greater than or equal to the value of
its parent, with the minimum-value element at the root.
Samples:
>>> heap = HeapBuilder()
>>> heap.array = [5, 4, 3, 2, 1]
>>> heap.generate_swaps()
>>> heap.swaps
[(1, 4), (0, 1), (1, 3)]
>>> # Explanation: After swapping elements 4 in position 1 and 1 in position
>>> # 4 the array becomes 5 1 3 2 4. After swapping elements 5 in position 0
>>> # and 1 in position 1 the array becomes 1 5 3 2 4. After swapping
>>> # elements 5 in position 1 and 2 in position 3 the array becomes
>>> # 1 2 3 5 4, which is already a heap, because a[0] = 1 < 2 = a[1],
>>> # a[0] = 1 < 3 = a[2], a[1] = 2 < 5 = a[3], a[1] = 2 < 4 = a[4].
>>> heap = HeapBuilder()
>>> heap.array = [1, 2, 3, 4, 5]
>>> heap.generate_swaps()
>>> heap.swaps
[]
>>> # Explanation: The input array is already a heap, because it is sorted
>>> # in increasing order.
"""
# def build_heap(data):
#     """Build a heap from ``data`` inplace.
#
#     Returns a sequence of swaps performed by the algorithm.
#     """
#     # The following naive implementation just sorts the given sequence
#     # using selection sort algorithm and saves the resulting sequence
#     # of swaps. This turns the given array into a heap, but in the worst
#     # case gives a quadratic number of swaps.
#     #
#     # TODO: replace by a more efficient implementation
#     swaps = []
#     for i in range(len(data)):
#         for j in range(i + 1, len(data)):
#             if data[i] > data[j]:
#                 swaps.append((i, j))
#                 data[i], data[j] = data[j], data[i]
#     return swaps
#
# def sift_down(index):
#     max_index = index
#

class Heap:
    def __init__(self):
        self.swaps = []
        self.nodes = []

    @property
    def size(self):
        return len(self.nodes)

    def read_nodes(self):
        self.nodes = [int(i) for i in input().split()]

    def left_child(self, index):
        """
        param index: index of the parent
        :return left child: index of the left child or -1 of there is no left child
        """
        left_child = 2 * index + 1
        if left_child >= self.size:
            return -1
        return left_child

    def right_child(self, index):
        """
        param index: index of the parent
        :return left child: index of the right child or -1 of there is no right child
        """
        right_child = 2 * index + 2
        if right_child >= self.size:
            return -1
        return right_child

    def sift_down(self, index):
        min_index = index
        left = self.left_child(index)
        right = self.right_child(index)
        if left != -1 and left <= self.size and self.nodes[left] < self.nodes[min_index]:
            min_index = left
        if left != -1 and right <= self.size and self.nodes[right] < self.nodes[min_index]:
            min_index = right

        if index != min_index:
            self.swaps.append((index, min_index))
            self.nodes[index], self.nodes[min_index] = self.nodes[min_index], self.nodes[index]
            self.sift_down(min_index)

    def heap(self):
        for i in range(self.size // 2, -1, -1):
            self.sift_down(i)

    def build_heap(self, data):
        self.nodes = [int(i) for i in data]
        self.heap()
        return self.swaps


def main():
    heap = Heap()
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = heap.build_heap(data)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
