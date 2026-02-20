from __future__ import annotations


def can_jump(nums: list[int]) -> bool:
    goal = len(nums) - 1
    for i in range(len(nums) - 2, -1, -1):
        if i + nums[i] >= goal:
            goal = i
    return goal == 0


def max_subarray(nums: list[int]) -> int:
    best = nums[0]
    cur = nums[0]

    for n in nums[1:]:
        cur = max(n, cur + n)
        best = max(best, cur)

    return best
