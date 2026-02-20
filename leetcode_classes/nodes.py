from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any


@dataclass
class ListNode:
    val: int = 0
    next: ListNode | None = None


@dataclass
class DoublyListNode:
    val: int = 0
    prev: DoublyListNode | None = None
    next: DoublyListNode | None = None


@dataclass
class RandomListNode:
    val: int = 0
    next: RandomListNode | None = None
    random: RandomListNode | None = None


@dataclass
class TreeNode:
    val: int = 0
    left: TreeNode | None = None
    right: TreeNode | None = None


@dataclass
class NaryNode:
    val: int = 0
    children: list[NaryNode] = field(default_factory=list)


@dataclass
class Node:
    """Generic graph node."""

    val: Any = None
    neighbors: list[Node] = field(default_factory=list)
