from __future__ import annotations

import os
import sys

if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lc.nodes import TreeNode
from lc.tree import build_tree


class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))


def run() -> None:
    root = build_tree([3, 9, 20, None, None, 15, 7])
    print(Solution().maxDepth(root))


if __name__ == "__main__":
    run()
