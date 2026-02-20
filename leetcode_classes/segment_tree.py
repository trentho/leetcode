from __future__ import annotations


class SegmentTreeSum:
    """Iterative segment tree for range sum + point update."""

    def __init__(self, nums: list[int]) -> None:
        self.n = len(nums)
        self.tree = [0] * (2 * self.n)
        for i, v in enumerate(nums):
            self.tree[self.n + i] = v
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, value: int) -> None:
        pos = self.n + index
        self.tree[pos] = value
        pos //= 2
        while pos > 0:
            self.tree[pos] = self.tree[pos * 2] + self.tree[pos * 2 + 1]
            pos //= 2

    def query(self, left: int, right: int) -> int:
        """Inclusive range query [left, right]."""
        left += self.n
        right += self.n
        out = 0

        while left <= right:
            if left % 2 == 1:
                out += self.tree[left]
                left += 1
            if right % 2 == 0:
                out += self.tree[right]
                right -= 1
            left //= 2
            right //= 2

        return out
