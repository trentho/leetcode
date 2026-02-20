from __future__ import annotations


def climb_stairs(n: int) -> int:
    if n <= 2:
        return n

    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b


def house_robber(nums: list[int]) -> int:
    rob1 = 0
    rob2 = 0
    for n in nums:
        rob1, rob2 = rob2, max(rob2, rob1 + n)
    return rob2
