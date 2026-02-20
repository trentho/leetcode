from __future__ import annotations


def subsets(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    cur: list[int] = []

    def dfs(i: int) -> None:
        if i == len(nums):
            out.append(cur.copy())
            return

        cur.append(nums[i])
        dfs(i + 1)
        cur.pop()

        dfs(i + 1)

    dfs(0)
    return out


def permutations(nums: list[int]) -> list[list[int]]:
    out: list[list[int]] = []
    used = [False] * len(nums)
    cur: list[int] = []

    def dfs() -> None:
        if len(cur) == len(nums):
            out.append(cur.copy())
            return

        for i in range(len(nums)):
            if used[i]:
                continue
            used[i] = True
            cur.append(nums[i])
            dfs()
            cur.pop()
            used[i] = False

    dfs()
    return out
