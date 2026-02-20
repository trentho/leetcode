from __future__ import annotations


def two_sum_sorted(nums: list[int], target: int) -> list[int]:
    """Template: two pointers on sorted array."""
    left = 0
    right = len(nums) - 1

    while left < right:
        cur = nums[left] + nums[right]
        if cur == target:
            return [left, right]
        if cur < target:
            left += 1
        else:
            right -= 1

    return []


def reverse_in_place(chars: list[str]) -> None:
    """Template: opposing two pointers in-place."""
    left = 0
    right = len(chars) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
