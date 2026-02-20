from __future__ import annotations

import unittest

from leetcode_classes import (
    FenwickTree,
    SegmentTreeSum,
    Trie,
    UnionFind,
    build_linked_list,
    build_tree,
    linked_list_to_list,
    tree_to_level_list,
)


class TestLeetCodeClasses(unittest.TestCase):
    def test_linked_list_helpers(self) -> None:
        head = build_linked_list([1, 2, 3, 4])
        self.assertEqual(linked_list_to_list(head), [1, 2, 3, 4])

    def test_tree_helpers(self) -> None:
        root = build_tree([3, 9, 20, None, None, 15, 7])
        self.assertEqual(tree_to_level_list(root), [3, 9, 20, None, None, 15, 7])

    def test_trie(self) -> None:
        trie = Trie()
        trie.insert("leet")
        self.assertTrue(trie.search("leet"))
        self.assertTrue(trie.starts_with("lee"))
        self.assertFalse(trie.search("lee"))

    def test_union_find(self) -> None:
        uf = UnionFind(5)
        self.assertTrue(uf.union(0, 1))
        self.assertTrue(uf.union(1, 2))
        self.assertEqual(uf.find(0), uf.find(2))
        self.assertFalse(uf.union(0, 2))

    def test_fenwick_tree(self) -> None:
        fw = FenwickTree(5)
        fw.add(0, 2)
        fw.add(1, 3)
        fw.add(2, 5)
        self.assertEqual(fw.prefix_sum(2), 10)
        self.assertEqual(fw.range_sum(1, 2), 8)

    def test_segment_tree_sum(self) -> None:
        st = SegmentTreeSum([1, 2, 3, 4])
        self.assertEqual(st.query(1, 3), 9)
        st.update(2, 10)
        self.assertEqual(st.query(1, 3), 16)


if __name__ == "__main__":
    unittest.main()
