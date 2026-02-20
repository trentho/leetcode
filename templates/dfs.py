from __future__ import annotations

from leetcode_classes.nodes import TreeNode


def dfs_recursive_graph(adj: list[list[int]], start: int) -> list[int]:
    """Template: recursive DFS on graph adjacency list."""
    seen = [False] * len(adj)
    order: list[int] = []

    def dfs(node: int) -> None:
        seen[node] = True
        order.append(node)
        for nei in adj[node]:
            if not seen[nei]:
                dfs(nei)

    dfs(start)
    return order


def dfs_iterative_graph(adj: list[list[int]], start: int) -> list[int]:
    """Template: iterative DFS using explicit stack."""
    stack = [start]
    seen = [False] * len(adj)
    order: list[int] = []

    while stack:
        node = stack.pop()
        if seen[node]:
            continue
        seen[node] = True
        order.append(node)

        for nei in reversed(adj[node]):
            if not seen[nei]:
                stack.append(nei)

    return order


def dfs_tree_max_depth(root: TreeNode | None) -> int:
    """Template: DFS recursion on tree."""
    if root is None:
        return 0
    return 1 + max(dfs_tree_max_depth(root.left), dfs_tree_max_depth(root.right))
