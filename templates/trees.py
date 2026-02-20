from __future__ import annotations

from collections import deque

from leetcode_classes.nodes import TreeNode


def max_depth(root: TreeNode | None) -> int:
    if root is None:
        return 0
    return 1 + max(max_depth(root.left), max_depth(root.right))


def level_order(root: TreeNode | None) -> list[list[int]]:
    if root is None:
        return []

    out: list[list[int]] = []
    q: deque[TreeNode] = deque([root])

    while q:
        level: list[int] = []
        for _ in range(len(q)):
            node = q.popleft()
            level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        out.append(level)

    return out
