from __future__ import annotations


def count_bits(n: int) -> list[int]:
    out = [0] * (n + 1)
    for i in range(1, n + 1):
        out[i] = out[i >> 1] + (i & 1)
    return out


def single_number(nums: list[int]) -> int:
    ans = 0
    for n in nums:
        ans ^= n
    return ans
