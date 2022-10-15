# python3
"""Computes height of a given tree.
Height of a (rooted) tree is the maximum depth of a node, or the maximum
distance from a leaf to the root.
Samples:
>>> tree = TreeHeight()
>>> tree.n = 5
>>> tree.parent = [4, -1, 4, 1, 1]
>>> tree.compute_height()
3
>>> # Explanation:
>>> # The input means that there are 5 nodes with numbers from 0 to 4,
>>> # node 0 is a child of node 4, node 1 is the root, node 2 is a child of
>>> # node 4, node 3 is a child of node 1 and node 4 is a child of node 1.
>>> #
>>> #       root
>>> #         1
>>> #        /|
>>> #       3 4
>>> #      /  |
>>> #     0   2
>>> #
>>> tree = TreeHeight()
>>> tree.n = 5
>>> tree.parent = [-1, 0, 4, 0, 3]
>>> tree.compute_height()
4
>>> # Explanation:
>>> # The input means that there are 5 nodes with numbers from 0 to 4,
>>> # node 0 is the root, node 1 is a child of node 0, node 2 is a child of
>>> # node 4, node 3 is a child of node 0 and node 4 is a child of node 3.
>>> #
>>> #       root
>>> #         1
>>> #        /|
>>> #       1 3
>>> #         |
>>> #         4
>>> #         |
>>> #         2
"""
import sys
import threading

sys.setrecursionlimit(10 ** 7)  # max depth of recursion
threading.stack_size(2 ** 27)  # new thread will get stack of such size


class TreeHeight:
    def read(self):
        self.n = int(sys.stdin.readline())
        self.parent = list(map(int, sys.stdin.readline().split()))

    def compute_height(self):

        # Replace this code with a faster implementation
        max_height = 0
        for vertex in range(self.n):
            height = 0
            i = vertex
            while i != -1:
                height += 1
                i = self.parent[i]
            max_height = max(max_height, height)
        return max_height


def main():
    tree = TreeHeight()
    tree.read()
    print(tree.compute_height())


threading.Thread(target=main).start()
