from __future__ import annotations


def two_sum(nums: list[int], target: int) -> list[int]:
    seen: dict[int, int] = {}
    for i, n in enumerate(nums):
        need = target - n
        if need in seen:
            return [seen[need], i]
        seen[n] = i
    return []


def group_anagrams(words: list[str]) -> list[list[str]]:
    groups: dict[tuple[int, ...], list[str]] = {}
    for word in words:
        freq = [0] * 26
        for ch in word:
            freq[ord(ch) - ord("a")] += 1
        key = tuple(freq)
        groups.setdefault(key, []).append(word)
    return list(groups.values())
