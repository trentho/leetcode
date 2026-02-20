from __future__ import annotations


def binary_search_exact(nums: list[int], target: int) -> int:
    """Template: exact match binary search."""
    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = left + (right - left) // 2
        if nums[mid] == target:
            return mid
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def lower_bound(nums: list[int], target: int) -> int:
    """Template: first index i where nums[i] >= target."""
    left = 0
    right = len(nums)

    while left < right:
        mid = left + (right - left) // 2
        if nums[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left
