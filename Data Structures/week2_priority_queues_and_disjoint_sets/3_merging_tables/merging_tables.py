# python3
"""Simulates a sequence of merge operations with tables in a database.
Samples:
>>> s = DisjointSet(5, [1, 1, 1, 1, 1])
>>> s.merge(3, 5)
>>> print(s.get_max_lines())
2
>>> s.merge(2, 4)
>>> print(s.get_max_lines())
2
>>> s.merge(1, 4)
>>> print(s.get_max_lines())
3
>>> s.merge(5, 4)
>>> print(s.get_max_lines())
5
>>> s.merge(5, 3)
>>> print(s.get_max_lines())
5
>>> # Explanation:
>>> # In this sample, all the tables initially have exactly 1 row of data.
>>> # Consider the merging operations:
>>> # 1. All the data from the table 5 is copied to table number 3.
>>> # Table 5 now contains only a symbolic link to table 3, while table 3
>>> # has 2 rows. 2 becomes the new maximum size.
>>> # 2. 2 and 4 are merged in the same way as 3 and 5.
>>> # 3. We are trying to merge 1 and 4, but 4 has a symbolic link pointing
>>> # to 2, so we actually copy all the data from the table number 2 to
>>> # the table number 1, clear the table number 2 and put a symbolic link
>>> # to the table number 1 in it. Table 1 now has 3 rows of data,
>>> # and 3 becomes the new maximum size.
>>> # 4. Traversing the path of symbolic links from 4 we have 4 → 2 → 1,
>>> # and the path from 5 is 5 → 3. So we are actually merging tables
>>> # 3 and 1. We copy all the rows from the table number 1 into the table
>>> # number 3, and now the table number 3 has 5 rows of data, which is
>>> # the new maximum.
>>> # 5. All tables now directly or indirectly point to table 3, so all
>>> # other merges won’t change anything.
>>>
>>> s = DisjointSet(6, [10, 0, 5, 0, 3, 3])
>>> s.merge(6, 6)
>>> print(s.get_max_lines()
10
>>> s.merge(6, 5)
>>> print(s.get_max_lines())
10
>>> s.merge(5, 4)
>>> print(s.get_max_lines())
10
>>> s.merge(4, 3)
>>> print(s.get_max_lines())
11
>>>
>>> # Explanation:
>>> # In this example tables have different sizes.
>>> # Let us consider the operations:
>>> # 1. Merging the table number 6 with itself doesn’t change anything,
>>> # and the maximum size is 10 (table number 1).
>>> # 2. After merging the table number 5 into the table number 6,
>>> # the table number 5 is cleared and has size 0, while the table number 6
>>> # has size 6. Still, the maximum size is 10.
>>> # 3. By merging the table number 4 into the table number 5, we actually
>>> # merge the table number 4 into the table number 6 (table 5 now contains
>>> # just a symbolic link to table 6), so the table number 4 is cleared and
>>> # has size 0, while the table number 6 has size 6.
>>> # Still, the maximum size is 10.
>>> # 4. By merging the table number 3 into the table number 4, we actually
>>> # merge the table number 3 into the table number 6 (table 4 now contains
>>> # just a symbolic link to table 6), so the table number 3 is cleared and
>>> # has size 0, while the table number 6 has size 11,
>>> # which is the new maximum size.
"""


class Database:
    def __init__(self, row_counts):
        self.row_counts = row_counts
        self.max_row_count = max(row_counts)
        n_tables = len(row_counts)
        self.ranks = [1] * (n_tables + 1)
        self.parents = list(range(n_tables + 1))
        self.lines = [0] + row_counts

    def merge(self, src, dst):
        src_parent = self.get_parent(src)
        dst_parent = self.get_parent(dst)

        if src_parent == dst_parent:
            return False

        # merge two components
        # use union by rank heuristic
        # update max_row_count with the new maximum table size
        if self.ranks[src_parent] >= self.ranks[dst_parent]:
            self.parents[src_parent] = dst_parent
        else:
            self.parents[dst_parent] = src_parent
            if self.ranks[src_parent] == self.ranks[dst_parent]:
                self.ranks[src_parent] += 1
        self.lines[dst_parent] += self.lines[src_parent]
        self.lines[src_parent] = 0
        if self.max_row_count < self.lines[dst_parent]:
            self.max_row_count = self.lines[dst_parent]
        return True

    def get_parent(self, table):
        # find parent/root
        parents_to_merge = []
        while table != self.parents[table]:
            parents_to_merge.append(self.parents[table])
            table = self.parents[table]
        # compress path
        for i in parents_to_merge:
            self.parents[i] = table
        return table


def main():
    n_tables, n_queries = map(int, input().split())
    counts = list(map(int, input().split()))
    assert len(counts) == n_tables
    db = Database(counts)
    for i in range(n_queries):
        dst, src = map(int, input().split())
        db.merge(dst, src)
        print(db.max_row_count)


if __name__ == "__main__":
    main()
