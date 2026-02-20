from __future__ import annotations


def fixed_window_max_sum(nums: list[int], k: int) -> int:
    """Template: fixed-size sliding window."""
    if k <= 0 or k > len(nums):
        return 0

    window_sum = sum(nums[:k])
    best = window_sum

    for right in range(k, len(nums)):
        window_sum += nums[right] - nums[right - k]
        best = max(best, window_sum)

    return best


def variable_window_longest_at_most_k_distinct(s: str, k: int) -> int:
    """Template: variable-size sliding window with frequency map."""
    if k <= 0:
        return 0

    left = 0
    count: dict[str, int] = {}
    best = 0

    for right, ch in enumerate(s):
        count[ch] = count.get(ch, 0) + 1

        while len(count) > k:
            left_ch = s[left]
            count[left_ch] -= 1
            if count[left_ch] == 0:
                del count[left_ch]
            left += 1

        best = max(best, right - left + 1)

    return best
