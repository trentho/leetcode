from __future__ import annotations

from collections import deque


class MonotonicQueueMax:
    """Queue that returns max in O(1), push/pop amortized O(1)."""

    def __init__(self) -> None:
        self._dq: deque[int] = deque()

    def push(self, value: int) -> None:
        while self._dq and self._dq[-1] < value:
            self._dq.pop()
        self._dq.append(value)

    def pop(self, value: int) -> None:
        if self._dq and self._dq[0] == value:
            self._dq.popleft()

    def max(self) -> int:
        return self._dq[0]


class MonotonicQueueMin:
    """Queue that returns min in O(1), push/pop amortized O(1)."""

    def __init__(self) -> None:
        self._dq: deque[int] = deque()

    def push(self, value: int) -> None:
        while self._dq and self._dq[-1] > value:
            self._dq.pop()
        self._dq.append(value)

    def pop(self, value: int) -> None:
        if self._dq and self._dq[0] == value:
            self._dq.popleft()

    def min(self) -> int:
        return self._dq[0]
