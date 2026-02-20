from __future__ import annotations


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix


def run() -> None:
    cases = [
        (["bat", "bag", "bank", "band"], "ba"),
        (["dance", "dag", "danger", "damage"], "da"),
        (["neet", "feet"], ""),
    ]

    solver = Solution()
    for strs, expected in cases:
        got = solver.longestCommonPrefix(strs)
        print(f"input={strs} expected={expected!r} got={got!r}")


if __name__ == "__main__":
    run()
