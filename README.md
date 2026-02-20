# LeetCode Python Driver

Reusable local framework for solving and debugging LeetCode problems in VS Code.

## Features

- Nodes: `ListNode`, `DoublyListNode`, `RandomListNode`, `TreeNode`, `NaryNode`, `Node`
- Linked list helpers: build/serialize + cycle detection
- Tree helpers: level-order build/serialize + BST helpers + inorder traversal
- Graph helpers: edge-list to adjacency (weighted/unweighted) + BFS order
- Core DS: `UnionFind`, `Trie`, `MinHeap`, `MaxHeap`, `FenwickTree`, `SegmentTreeSum`
- Interview utility DS: `Stack`, `Queue`, `MinStack`, monotonic queues
- Flat `problems/` module layout with dynamic runner in `main.py`
- Ready-to-copy algorithm templates in `templates/`

## Project Structure

```text
leetcode/
├── leetcode_classes/
│   ├── __init__.py
│   ├── nodes.py
│   ├── linked_list.py
│   ├── tree.py
│   ├── graph.py
│   ├── queue_stack.py
│   ├── heap.py
│   ├── trie.py
│   ├── fenwick_tree.py
│   ├── segment_tree.py
│   ├── monotonic.py
│   └── union_find.py
├── problems/
│   ├── __init__.py
│   ├── lc_0001_two_sum.py
│   ├── lc_0206_reverse_linked_list.py
│   └── lc_0104_max_depth.py
├── tests/
├── templates/
│   ├── sliding_window.py
│   ├── bfs.py
│   ├── dfs.py
│   ├── two_pointers.py
│   └── binary_search.py
├── main.py
└── requirements.txt
```

## Usage

Run from the project root:

```bash
python3 main.py lc_0104_max_depth
python3 main.py lc_0206_reverse_linked_list
```

Each problem module should expose a `run()` function.

## Templates

Use the boilerplates in `templates/` as quick starters:

- `templates/sliding_window.py`
- `templates/bfs.py`
- `templates/dfs.py`
- `templates/two_pointers.py`
- `templates/binary_search.py`

## VS Code Debugging

1. Open this repo in VS Code.
2. Set breakpoints in a problem file or helper module.
3. Start debugging `main.py` with an argument such as:
   - `lc_0104_max_depth`

## LeetCode Compatibility Tip

If you want a single file that runs both locally and on LeetCode:

```python
try:
    from leetcode_classes.nodes import TreeNode
except ImportError:
    pass
```
