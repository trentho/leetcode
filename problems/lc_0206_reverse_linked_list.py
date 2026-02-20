from __future__ import annotations

import os
import sys

if __package__ is None or __package__ == "":
    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from lc.linked_list import build_linked_list, print_linked_list
from lc.nodes import ListNode


class Solution:
    def reverseList(self, head: ListNode | None) -> ListNode | None:
        prev: ListNode | None = None
        cur = head

        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return prev


def run() -> None:
    head = build_linked_list([1, 2, 3, 4, 5])
    result = Solution().reverseList(head)
    print_linked_list(result)


if __name__ == "__main__":
    run()
