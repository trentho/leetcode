from __future__ import annotations


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, n in enumerate(nums):
            want = target - n
            if want in seen:
                return [seen[want], i]
            seen[n] = i
        return []


def run() -> None:
    nums = [2, 7, 11, 15]
    target = 9
    print(Solution().twoSum(nums, target))


if __name__ == "__main__":
    run()
