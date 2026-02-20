from __future__ import annotations

import heapq


def k_closest(nums: list[int], k: int, x: int) -> list[int]:
    heap: list[tuple[int, int]] = []
    for n in nums:
        heapq.heappush(heap, (abs(n - x), n))
    out = [heapq.heappop(heap)[1] for _ in range(min(k, len(heap)))]
    return sorted(out)


def k_largest(nums: list[int], k: int) -> list[int]:
    if k <= 0:
        return []
    min_heap: list[int] = []
    for n in nums:
        heapq.heappush(min_heap, n)
        if len(min_heap) > k:
            heapq.heappop(min_heap)
    return sorted(min_heap, reverse=True)
