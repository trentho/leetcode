from __future__ import annotations

from collections import deque

from .nodes import TreeNode


def build_tree(level: list[int | None]) -> TreeNode | None:
    """Build a binary tree from LeetCode-style level-order input."""
    if not level or level[0] is None:
        return None

    root = TreeNode(level[0])
    q: deque[TreeNode] = deque([root])
    i = 1

    while q and i < len(level):
        node = q.popleft()

        if i < len(level) and level[i] is not None:
            node.left = TreeNode(level[i])
            q.append(node.left)
        i += 1

        if i < len(level) and level[i] is not None:
            node.right = TreeNode(level[i])
            q.append(node.right)
        i += 1

    return root


def tree_to_level_list(root: TreeNode | None) -> list[int | None]:
    if root is None:
        return []

    out: list[int | None] = []
    q: deque[TreeNode | None] = deque([root])

    while q:
        node = q.popleft()
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        q.append(node.left)
        q.append(node.right)

    while out and out[-1] is None:
        out.pop()

    return out


def print_tree_level(root: TreeNode | None) -> None:
    print(tree_to_level_list(root))


def bst_insert(root: TreeNode | None, val: int) -> TreeNode:
    if root is None:
        return TreeNode(val)

    cur = root
    while True:
        if val < cur.val:
            if cur.left is None:
                cur.left = TreeNode(val)
                return root
            cur = cur.left
        else:
            if cur.right is None:
                cur.right = TreeNode(val)
                return root
            cur = cur.right


def build_bst(values: list[int]) -> TreeNode | None:
    root: TreeNode | None = None
    for v in values:
        root = bst_insert(root, v)
    return root


def inorder(root: TreeNode | None) -> list[int]:
    out: list[int] = []

    def dfs(node: TreeNode | None) -> None:
        if node is None:
            return
        dfs(node.left)
        out.append(node.val)
        dfs(node.right)

    dfs(root)
    return out
