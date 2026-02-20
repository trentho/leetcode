from __future__ import annotations

from collections import deque

from leetcode_classes.nodes import TreeNode

def bfs_graph(adj: list[list[int]], start: int) -> list[int]:
    """Template: BFS on adjacency-list graph."""
    seen = [False] * len(adj)
    q: deque[int] = deque([start])
    seen[start] = True
    order: list[int] = []

    while q:
        node = q.popleft()
        order.append(node)
        for nei in adj[node]:
            if not seen[nei]:
                seen[nei] = True
                q.append(nei)

    return order


def bfs_tree_by_level(root: TreeNode | None) -> list[list[int]]:
    """Template: level-order traversal for binary tree."""
    if root is None:
        return []

    q: deque[TreeNode] = deque([root])
    levels: list[list[int]] = []

    while q:
        level_size = len(q)
        level: list[int] = []

        for _ in range(level_size):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)

        levels.append(level)

    return levels
