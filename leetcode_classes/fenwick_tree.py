from __future__ import annotations


class FenwickTree:
    """Binary Indexed Tree supporting point updates + prefix/range sum."""

    def __init__(self, n: int) -> None:
        self.n = n
        self.bit = [0] * (n + 1)

    def add(self, index: int, delta: int) -> None:
        i = index + 1
        while i <= self.n:
            self.bit[i] += delta
            i += i & -i

    def prefix_sum(self, index: int) -> int:
        if index < 0:
            return 0
        i = index + 1
        out = 0
        while i > 0:
            out += self.bit[i]
            i -= i & -i
        return out

    def range_sum(self, left: int, right: int) -> int:
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
