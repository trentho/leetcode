from __future__ import annotations

from collections import deque


class Stack:
    def __init__(self) -> None:
        self._data: list[int] = []

    def push(self, value: int) -> None:
        self._data.append(value)

    def pop(self) -> int:
        return self._data.pop()

    def peek(self) -> int:
        return self._data[-1]

    def empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class Queue:
    def __init__(self) -> None:
        self._data: deque[int] = deque()

    def push(self, value: int) -> None:
        self._data.append(value)

    def pop(self) -> int:
        return self._data.popleft()

    def peek(self) -> int:
        return self._data[0]

    def empty(self) -> bool:
        return not self._data

    def __len__(self) -> int:
        return len(self._data)


class MinStack:
    def __init__(self) -> None:
        self._vals: list[int] = []
        self._mins: list[int] = []

    def push(self, val: int) -> None:
        self._vals.append(val)
        if not self._mins:
            self._mins.append(val)
        else:
            self._mins.append(min(val, self._mins[-1]))

    def pop(self) -> int:
        self._mins.pop()
        return self._vals.pop()

    def top(self) -> int:
        return self._vals[-1]

    def get_min(self) -> int:
        return self._mins[-1]

    def __len__(self) -> int:
        return len(self._vals)
