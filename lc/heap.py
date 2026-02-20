from __future__ import annotations

import heapq


class MinHeap:
    def __init__(self, values: list[int] | None = None) -> None:
        self._h = values[:] if values else []
        heapq.heapify(self._h)

    def push(self, val: int) -> None:
        heapq.heappush(self._h, val)

    def pop(self) -> int:
        return heapq.heappop(self._h)

    def peek(self) -> int:
        return self._h[0]

    def __len__(self) -> int:
        return len(self._h)


class MaxHeap:
    def __init__(self, values: list[int] | None = None) -> None:
        self._h = [-v for v in values] if values else []
        heapq.heapify(self._h)

    def push(self, val: int) -> None:
        heapq.heappush(self._h, -val)

    def pop(self) -> int:
        return -heapq.heappop(self._h)

    def peek(self) -> int:
        return -self._h[0]

    def __len__(self) -> int:
        return len(self._h)
